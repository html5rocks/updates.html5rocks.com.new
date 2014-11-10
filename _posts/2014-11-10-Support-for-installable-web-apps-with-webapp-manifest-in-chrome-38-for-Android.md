---
layout: post
title: "Support for installable Web Apps with WebApp Manifest in Chrome 38 for Android"
description: "Use the WebApp manifest to control how your web app launches"
article:
  written_on: 2014-11-10
  updated_on: 2014-11-10
authors:
  - paulkinlan
tags:
  - mobile
  - front-end
permalink: /2014/11/Support-for-installable-web-apps-with-webapp-manifest-in-chrome-38-for-Android
---

For Web Apps to be successful they need to work how the user would expect an native application to work. The [Manifest for Web applications](https://w3c.github.io/manifest/) gives you the developer the ability to control what to launch and more importantly *how* to launch it.

Chrome has had this feature since Chrome 38 for Android and it gives you the control over.  How the web appears when it is installed to the homescreen via the `name` and `icons` properties and how it should be launched when the user clicks on the icon with the `start_url`, `display` and `orientation`.

{% highlight json %}
{
  "name": "Kinlan's Amaze App",
  "icons": [
    {
      "src": "launcher-icon-0-75x.png",
      "sizes": "36x36",
      "type": "image/png",
      "density": "0.75"
    },
    {
      "src": "launcher-icon-1x.png",
      "sizes": "48x48",
      "type": "image/png",
      "density": "1.0"
    },
    {
      "src": "launcher-icon-1-5x.png",
      "sizes": "72x72",
      "type": "image/png",
      "density": "1.5"
    },
    {
      "src": "launcher-icon-2x.png",
      "sizes": "96x96",
      "type": "image/png",
      "density": "2.0"
    },
    {
      "src": "launcher-icon-3x.png",
      "sizes": "144x144",
      "type": "image/png",
      "density": "3.0"
    },
    {
      "src": "launcher-icon-4x.png",
      "sizes": "192x192",
      "type": "image/png",
      "density": "4.0"
    }
  ],
  "start_url": "index.html",
  "display": "standalone",
  "orientation": "landscape"
}
{% endhighlight %}

Once you have the manifest and it is hosted on your site,

{% highlight html %}
<link rel="manifest" href="manifest.json">
{% endhighlight %}

## What every developer should do today

This feature is entirely progressive and allows you create better, more integrated experiences for users that are using a browser that supports the feature.  As of Nov 2014 Chrome has implemented the manifest, Opera and Mozilla are implementing and [IE is exploring the area](https://status.modern.ie/webapplicationmanifest?term=manifest).

### Utility Apps

The majority of games will benifit from this immedidately,
*  Add a manifest
*  Add icons
*  Tell it to launch full screen

### Games 

The majority of games will benifit from this immedidately,
*  Add a manifest
*  Add icons
*  Tell the app to launch full screen
*  Tell the app to launch in the orientation that you want the game to be played in.

### Sites

## Detecting if you are launched from the homescreen?

A question that keeps popping up about Chrome's implementation of "mobile-web-app-capable" is: How can I tell if
I am running as launched from the homescreen?  On iOS you can use `navigator.standalone` to see if it is running
like a native app, but we don't have this on Chrome for Android.

The simple answer is: Add a query string parameter to your `start_url` that indicates how it was launched.  For example `start_url: /index.html?standalone=true`

## Learning More

Check out Chrome's guidance for [Add to homescree](https://developer.chrome.com/multidevice/android/installtohomescreen#supporting) the [HTML5Doctor](http://html5doctor.com/web-manifest-specification/) for a deeper dive in 
to where the future of the spec and implementations will be

## Diving deep

Let's face it, the majority of us love to see under the hood about how a feature is implemented, it lets us learn more about the systems and also helps us track when changes occur that might give us early access to new features for our users.

If like me your are interested about how this is implemented in Chrome here are some useful links:
*  The [logic for parsing the data](https://code.google.com/p/chromium/codesearch#chromium/src/chrome/browser/android/shortcut_helper.cc&sq=package:chromium&q=file:shortcut_helper.cc&l=1) from the manifest (including what do with fallbacks)
*  [OnDidGetManifest](https://code.google.com/p/chromium/codesearch#chromium/src/chrome/browser/android/shortcut_helper.cc&l=233) - This is where Chrome does all the grunt work and you can see what parameters are supported.
*  The code for showing the [Add to homescreen UI](https://code.google.com/p/chromium/codesearch#chromium/src/chrome/android/java/src/org/chromium/chrome/browser/webapps/AddToHomescreenDialog.java&sq=package:chromium)
