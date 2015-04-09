---
layout: post
title: "DOM Attributes now on the prototype chain"
description: ""
article:
  written_on: 2015-04-09
  updated_on: 2015-04-09
authors:
  - paulkinlan
tags:
  - DOM
  - API change
permalink: /2015/04/DOM-attributes-now-on-the-prototype
---

The Chrome team recently [announced that we are moving DOM attributes to the prototype chain](https://groups.google.com/a/chromium.org/forum/#!topic/blink-dev/H0MGw0jkdn4).  This change, implemented in Chrome 43, brings Chrome inline with the spec and other browsers’ implementations, such as IE and Firefox.  WebKit based browsers, such as Safari, are currently not compatible with the spec. 

The new behavior is positive in many ways. It:

* Improves compatibility across the web (IE and Firefox do this already) via compliance with the spec.
* Allows you to efficiently create getters/setters on every DOM object. 
* Increases the hackability of DOM programming. For example, it will enable you to implement Polyfills that allow you to efficiently emulate functionality missing in some browsers and JavaScript libraries that override default DOM attribute behaviors. 

It can however cause some issues for developers, especially if you were relying on this behaviour because of legacy compatibility between Chrome and WebKit so we encourage you to check your site and see the summary of changes.

## Summary of Changes

### Using `hasOwnProprery` on a DOM Object instance will now return `false`

Sometimes developers will use `hasOwnProperty` to check for presence of an attribute on an object.  This will no longer work as [per the spec](http://www.ecma-international.org/ecma-262/5.1/#sec-15.2.4.5) because objects are not considered on the protoype chain.

Chrome 42 and earlier 

{% highlight javascript %}
> div = document.createElement("div");
> div.hasOwnProperty("isContentEditable");

true
{% endhighlight %}

Chrome 43 onwards

{% highlight javascript %}
> div = document.createElement("div");
> div.hasOwnProperty("isContentEditable");

false
{% endhighlight %}

This now means if you want to see if `isContentEditable` is available on the element you will have follow the prototype chain on the DOM Object instance. For example HTMLDivElement inherits from HTMLElement which defines the `isContentEditable` attibute.

{% highlight javascript %}
> div.__proto__.__proto__.hasOwnProperty("isContentEditable");

true
{% endhighlight %}

### Object.getOwnPropertyDescriptor on DOM Object Instance will no longer return a property descriptor for Attributes.

If your site needs to get the property descriptor of an Attribute on DOM Objects, you will now need to follow the prototype chain.

If you wanted to get the propery description in Chrome 42 and earlier you would have done:

{% highlight javascript %}
> Object.getOwnPropertyDescriptor(div, "id");

Object {value: "", writable: true, enumerable: true, configurable: true}
{% endhighlight %}

Chrome 43 onwards will return `undefined` in this screnario.

{% highlight javascript %}
> Object.getOwnPropertyDescriptor(div, "id");

undefined
{% endhighlight %}

Which means to now get the property descriptor for the "id" attribute you will need to follow the prototype chain as follows:

{% highlight javascript %}
> Object.getOwnPropertyDescriptor(div.__proto__.__proto__, "id");

Object {get: function, set: function, enumerable: false, configurable: false}
{% endhighlight %}

### JSON.stringify will no longer serialize DOM Attributes

JSON.stringify doesn’t serialize DOM Attributes on the prototype.  For example, this can affect your site if you are trying to serialize an object such as Push Notification's [PushSubscription](https://w3c.github.io/push-api/#pushsubscription-interface).

Chrome 42 and earlier

{% highlight javascript %}
> JSON.stringify(subscription);

{
  "endpoint": "https://something",
  "subscriptionId": "SomeID"
}
{% endhighlight %}

Chrome 43 onwards will not serialize the elements.

{% highlight javascript %}
> JSON.stringify(subscription);

{}
{% endhighlight %}

### Writing to read-only properties in strict mode will throw an error

Writing to read-only properties is supposed to throw an exception when you are using strict mode. For example, take the following:

{% highlight javascript %}
function foo() {
  "use strict";
  var d = document.createElement("div");
  console.log(d.isContentEditable);
  d.isContentEditable = 1;
  console.log(d.isContentEditable);
}
{% endhighlight %}

Chrome 42 and earlier the function would have continued and siliently carried on executing the function, although `isContentEditable` would have not been changed.

{% highlight javascript %}// Chrome 42 and earlier behavior
> foo();

false // isContentEditable
false // isContentEditable (after writing to read-only property)
{% endhighlight %}

Now in Chrome 43 and onwards there will be an exception thrown.

{% highlight javascript %}// Chrome 43 and onwards behavior
> foo();

false
Uncaught TypeError: Cannot set property isContentEditable of #<HTMLElement> which has only a getter
{% endhighlight %}