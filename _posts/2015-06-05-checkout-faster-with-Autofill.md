---
layout: post
title: "Help users checkout faster with Autofill"
description: "Help users checkout faster with Autofill. We’ve found that by correctly using autocomplete attributes on your forms, users complete them up to 30% faster!"
article:
  written_on: 2015-06-05
  updated_on: 2015-06-05
authors:
  - idogreen
tags:
  - forms
  - autofill
  - monetization
permalink: /2015/06/checkout-faster-with-Autofill

---

### Help users checkout faster with Autofill

People hate filling out web forms, especially on mobile devices. They can be 
slow and frustrating to complete and often contain multi-page steps and 
validation issues. This leads to high user drop-off and frustration. To help 
make things easier for users, browsers have long been able to autocomplete 
fields on behalf of the user. Chrome took this a step further in 2011 by 
introducing [Autofill](https://support.google.com/chrome/answer/142893?hl=en), 
which fills in entire forms based on a user's Autofill profile.

Starting in the next major version of Chrome (M43), we're taking yet another 
step to help users fill out forms faster by expanding our support for credit 
cards and addresses in Google. This means that the same information users use to 
purchase things inside of the Google Play store are now available to them on 
websites. By using the standard _autocomplete_ attributes, you can ensure your 
users' happiness by helping Chrome autofill your checkout forms with 100% 
accuracy.

Autocomplete attributes are a way for you, the developer, to control how the 
browser should populate a given form field.  For example, if you are expecting a 
street address you can hint to the browser that you are expecting it by using 
_autocomplete="address-line1"_. This prevents the browser from incorrectly 
guessing form fields on your website which can result in a poor user experience.

We've found that by correctly using autocomplete attributes on your forms, users 
complete them up to 30% faster. And since _autocomplete_ is part of the [WHATWG 
](https://html.spec.whatwg.org/multipage/forms.html#autofill)[HTML](https://html.spec.whatwg.org/multipage/forms.html#autofill) 
standard, we hope that other browsers will support it in the near future.  
<img src="https://lh4.googleusercontent.com/kAeKrmA7eJhyxqcrilDShud36JNwpz04hFJIv7zYc0tPziwrx3q1Gqmas1OeSTVlcD-HOgteBWHbQPs=w1338-h685-rw" width="301" height="538" />  

In the past, many developers would add _autocomplete="off"_ to their form fields 
to prevent the browser from performing any kind of autocomplete functionality. 
While Chrome will still respect this tag for autocomplete data, it will not 
respect it for autofill data. So when should you use _autocomplete="off"_? One 
example is when you've implemented your own version of autocomplete for search. 
Another example is any form field where users will input and submit different 
kinds of information where it would not be useful to have the browser remember 
what was submitted previously.

The most common _autocomplete_ attributes are shown in the table below and are 
documented in [Web 
Fundamentals](https://developers.google.com/web/fundamentals/input/?hl=en). I've 
marked (red) the ones that are critical for credit cards and the checkout 
process.

### Common Attributes

<table>
<tr>
<td markdown="block">
**Content type**
</td>
<td markdown="block">
**name attribute**
</td>
<td markdown="block">
**autocomplete attribute**
</td>
</tr>
<tr>
<td markdown="block">
**Credit Card**
</td>
<td markdown="block">
**ccname**  
**cardnumber**  
**cvc**  
**ccmonth**  
**ccyear**  
**exp-date**  
**card-type**
</td>
<td markdown="block">
* **cc-name**
* **cc-number**
* **cc-csc**
* **cc-exp-month**
* **cc-exp-year**
* **cc-exp**
* **cc-type**
</td>
</tr>
<tr>
<td markdown="block">
Name
</td>
<td markdown="block">
name  
fname  
mname  
lname
</td>
<td markdown="block">
* name (full name)
* given-name (first name)
* additional-name (middle name)
* family-name (last name)
</td>
</tr>
<tr>
<td markdown="block">
Email
</td>
<td markdown="block">
email
</td>
<td markdown="block">
email
</td>
</tr>
<tr>
<td markdown="block">
Address
</td>
<td markdown="block">
address  
city  
region  
province  
state  
zip  
zip2  
postal  
country
</td>
<td markdown="block">
* For one address input:
    * street-address
* For two address inputs:
    * address-line1
    * address-line2
* address-level1 (state or province)
* address-level2 (city)
* postal-code (zip code)
* country
</td>
</tr>
<tr>
<td markdown="block">
Phone
</td>
<td markdown="block">
phone  
mobile  
country-code  
area-code  
exchange  
suffix  
ext
</td>
<td markdown="block">
tel
</td>
</tr>
</table>

   
The autocomplete attributes can be accompanied with a section name, such as:

* **shipping **given-name
* **billing **street-address<br/>

It is recommended because it will make your markup easier to parse and 
understand. The browser will autofill different sections separately and not as a 
continuous form.

### An example of a payment form

Code snippet:

&lt;label for="frmNameCC"&gt;Name on card&lt;/label&gt;  
&lt;input name="ccname" id="frmNameCC" required placeholder="Full Name" 
autocomplete="cc-name"&gt;    
&lt;label for="frmCCNum"&gt;Card Number&lt;/label&gt;  
&lt;input name="cardnumber" id="frmCCNum" required autocomplete="cc-number"&gt;    
&lt;label for="frmCCCVC"&gt;CVC&lt;/label&gt;  
&lt;input name="cvc" id="frmCCCVC" required autocomplete="cc-csc"&gt;  
  
&lt;label for="frmCCExp"&gt;Expiry&lt;/label&gt;  
&lt;input name="cc-exp" id="frmCCExp" required placeholder="MM-YYYY" 
autocomplete="cc-exp"&gt;

**Forms best practices**

1. **Use ****_labels_**** on form inputs**, and ensure they're visible when the 
   field is in focus. The label element provides direction to the user, telling 
   them what information is needed in a form element. Each label is associated 
   with an input element by placing it inside the label element. Applying labels 
   to form elements also helps to improve the touch target size: the user can 
   touch either the label or the input in order to place focus on the input 
   element.
1. **Use placeholder to provide guidance** about what you expect. The 
   placeholder attribute provides a hint to the user about what's expected in 
   the input, typically by displaying the value as light text until the the user 
   starts typing in the element. Placeholders disappear as soon as the user 
   starts typing in an element, thus they are not a replacement for labels. They 
   should be used as an aid to help guide users on the required format and 
   content.

### Demo

You can see it in action over at: 
[greenido.github.io/Product-Site-101/form-cc-example.html](https://greenido.github.io/Product-Site-101/form-cc-example.html)  
Or check the code: 
[https://github.com/greenido/Product-Site-101](https://github.com/greenido/Product-Site-101)

<img src="https://lh3.googleusercontent.com/oFnGbUaJq6iUyIX8yA0iITmjH7IUQ2oB-mI_87UMglzE7eS0u60wc90kamXDqKGERh4qSduSRc3dJas=w1338-h685-rw" width="212" height="314" />

