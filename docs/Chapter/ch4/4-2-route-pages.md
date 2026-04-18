WEBVTT

00:00.350 --> 00:05.840
All right, so in this video we're gonna learn about the process called routing.

00:05.840 --> 00:12.440
And you will see how to create individual pages in your Next.js app.

00:13.090 --> 00:16.810
So react itself is a library.

00:16.810 --> 00:21.280
It is responsible just for rendering the UIs.

00:21.280 --> 00:30.130
And one of the things that frameworks like Next.js gives you is it lets you create complete websites.

00:30.130 --> 00:34.300
And on a typical website you've got multiple pages.

00:34.300 --> 00:41.680
Now, since we have multiple pages, we need a way to tell which page to display at any given time.

00:42.310 --> 00:47.950
So every page is being identified by a unique URL.

00:49.320 --> 00:51.420
So take a look at this example.

00:51.420 --> 00:53.010
So you have domain.

00:53.010 --> 00:56.880
And after a slash you've got the path.

00:56.880 --> 01:01.440
So the path for every page is unique.

01:01.440 --> 01:08.730
And our Next.js application will take this path that comes after the domain.

01:08.730 --> 01:14.610
And it would route the visitor of your website to a specific page.

01:14.610 --> 01:18.660
And this is the process of routing.

01:20.340 --> 01:24.870
Next up, you should know that we're going to be using the app router.

01:24.870 --> 01:30.960
So for everyone who's new to Next.js this should make absolutely no difference.

01:30.960 --> 01:38.880
But if you've ever used Next.js before or you will have to work with some Next.js legacy applications.

01:38.880 --> 01:42.780
Previously there was a thing called Pages router.

01:42.780 --> 01:49.920
Well, it kind of still is a thing because the app router is a pretty new thing.

01:49.920 --> 01:53.760
Not everyone converted to the app router, though.

01:53.790 --> 01:59.460
Using the app router is recommended for all new and future applications.

01:59.700 --> 02:08.160
Now, just a note, I would like you to take a note that the app router is built on react server components,

02:08.160 --> 02:16.710
and all the pages that we build using the app router are by default rendered on the server.

02:16.800 --> 02:19.710
So don't worry about this too much.

02:19.710 --> 02:24.300
Just take a note because this will have some implications later on.

02:24.660 --> 02:31.200
Next, let's talk a little about how the routing actually works in Next.js.

02:31.880 --> 02:40.070
So the Next.js is using a file system based router, which has one huge benefit.

02:40.070 --> 02:44.180
It's super easy to understand and it is very intuitive.

02:44.660 --> 02:48.140
So you will use folders to define routes.

02:48.140 --> 02:55.490
You can nest folders inside other folders to create the path segments.

02:55.820 --> 03:04.640
And every time you would like to have a page for this specific folder, you just create a page dot js

03:04.640 --> 03:09.770
file inside and then this just becomes a public page.

03:11.460 --> 03:13.110
So let's see an image.

03:13.730 --> 03:21.950
So if you have a URL path like this dashboard slash settings to display a page.

03:21.950 --> 03:29.900
Under this URL, you will have to create the dashboard folder inside the app folder, and then settings

03:29.900 --> 03:32.750
folder inside the dashboard folder.

03:32.750 --> 03:41.120
And finally a page js file inside the settings folder so it can become a public route.

03:41.540 --> 03:47.240
Okay, so now let's jump to the code editor and let's create some routes and some pages.

03:48.170 --> 03:52.160
So we've already have one page the main page.

03:52.160 --> 04:01.520
So this page js file when located directly inside the app directory it will just display the main page

04:01.520 --> 04:03.050
of your website.

04:03.200 --> 04:07.700
Notice that I had to add this use client directive.

04:07.700 --> 04:08.960
Remember what I said?

04:08.960 --> 04:12.980
That by default pages are rendered on the server?

04:12.980 --> 04:21.800
Well, unless you use state, which can only make sense when the page is rendered on the client, then

04:21.800 --> 04:27.410
you need to mark every component that is using state with this directive.

04:27.410 --> 04:33.470
I'm going to go back to this later on just explaining things as we go.

04:33.710 --> 04:36.230
Okay, so we've got the main page.

04:36.230 --> 04:38.600
Why won't we create another page.

04:38.600 --> 04:41.990
Maybe let's call that about page.

04:41.990 --> 04:46.220
The page that would tell the user something about us.

04:46.340 --> 04:50.930
So you need to create a folder and call this about.

04:51.230 --> 04:57.560
Now if you visit this right now slash about is 404.

04:57.560 --> 05:02.450
So as I said you first need to create a page JS file.

05:02.450 --> 05:06.860
If you create other files in such folders it's fine.

05:06.860 --> 05:13.280
They can be located in this folder though that won't be a route that would display a page.

05:13.280 --> 05:18.650
So it has to be specifically named page JS.

05:19.730 --> 05:24.950
Okay, now we have a page, but we also need to create a component here.

05:26.680 --> 05:29.770
So let's create a component for this page.

05:29.770 --> 05:31.960
I am going to use a snippet.

05:31.960 --> 05:39.850
And the good convention is to always suffix the name of components that are pages with the page.

05:39.850 --> 05:42.940
So this would be about page.

05:42.940 --> 05:49.180
Also, remember that the name of the component should start with a capital letter, and I am using a

05:49.180 --> 05:50.080
fragment here.

05:50.080 --> 05:52.480
So an empty tag.

05:52.480 --> 05:55.570
And let me just say about me.

05:55.570 --> 06:01.630
So currently there is an error because this file does not export anything.

06:01.810 --> 06:05.290
But when I save the changes we see a page.

06:05.290 --> 06:08.620
So there is the main page and the about page.

06:09.880 --> 06:14.350
Okay, so let's nest something even one level deeper.

06:14.350 --> 06:21.400
So with the About Me page, I might also do a showcase of all my projects.

06:21.400 --> 06:27.670
So I create projects directory and page js inside this new directory.

06:27.670 --> 06:36.820
And another component let's call that projects page and let's say projects and save it.

06:38.020 --> 06:40.930
So now you can go to about projects.

06:40.930 --> 06:42.550
And as you see it also works.

06:42.550 --> 06:52.480
And this specific URL this path about slash projects is being uh routed to our projects page.
