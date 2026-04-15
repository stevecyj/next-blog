WEBVTT

00:00.290 --> 00:09.680
Now, you definitely notice this odd syntax of mixing the JavaScript directly with HTML.

00:09.710 --> 00:16.970
Now, if you would try that directly inside a plain HTML file, you can expect some errors.

00:16.970 --> 00:23.750
That's obviously either not valid HTML nor this is a valid JavaScript.

00:23.750 --> 00:29.630
And there is a reason for that because it's not HTML, not JavaScript.

00:29.630 --> 00:38.030
This syntax together is called JSX and it is mixing together JavaScript with HTML.

00:38.030 --> 00:40.220
And now let's talk about JSX.

00:41.770 --> 00:48.250
Now let's take a closer look at JSX by actually doing some hands on coding.

00:48.250 --> 00:56.500
So I have the project open on the left side, and will be having a preview of our development server

00:56.500 --> 00:58.420
inside the browser on the right.

00:58.420 --> 01:01.960
So the first step would be to start the next development server.

01:01.960 --> 01:09.040
You can do that directly from within the VSCode terminal by typing npm run dev.

01:09.070 --> 01:13.540
Now obviously this command can also be run directly in your terminal.

01:13.540 --> 01:19.150
So this should start up the next application that we have created previously.

01:19.360 --> 01:28.030
Now let's go into this app folder and open this specific file the pages.

01:28.060 --> 01:34.300
Now let's ignore everything that you can find inside this file.

01:34.300 --> 01:37.900
Because as you can see, there is tons of markup.

01:37.900 --> 01:42.850
And this basically renders this page that you can see in the browser.

01:42.850 --> 01:53.410
And I'd like you to select all this content starting from the main tag up to the main closing tag,

01:53.410 --> 01:59.620
and just remove all of that and also get rid of this import.

01:59.620 --> 02:04.630
Let's just leave this return statement and the brackets.

02:04.630 --> 02:07.390
And now let's zoom in a little.

02:08.350 --> 02:10.360
And now let's talk about JSX.

02:13.050 --> 02:13.290
Now.

02:13.290 --> 02:19.290
When you save changes immediately on the right in the browser, you will see an error, and that's due

02:19.290 --> 02:27.780
to a feature called Fast Refresh or Hot Module reloading, which will automatically refresh your next

02:27.780 --> 02:28.440
project.

02:28.440 --> 02:32.520
If you make any change to any file and you save it.

02:32.790 --> 02:35.670
Now let's go back to JSX syntax.

02:35.670 --> 02:46.230
So in short, the JSX syntax combines HTML like markup with JavaScript, and this enables your react

02:46.230 --> 02:52.020
components to include both rendering logic and UI structure.

02:52.050 --> 02:58.290
Now I'm gonna talk about the components themselves later on in detail as well.

02:58.320 --> 03:01.740
For now let's just focus on the JSX.

03:02.880 --> 03:08.460
So you will return this JSX syntax from those components.

03:08.460 --> 03:12.960
And I typically enclose that within brackets.

03:12.960 --> 03:22.740
Now one thing you have to know about JSX is that it always requires at least one root element.

03:22.740 --> 03:25.140
That can be a div, for example.

03:25.140 --> 03:27.990
But there can be only one element.

03:27.990 --> 03:32.730
You can't have two root elements like that.

03:32.760 --> 03:34.080
That's an error.

03:35.130 --> 03:38.220
So let's say hello from this element.

03:38.220 --> 03:44.220
And when I save it you should immediately see this hello text inside the browser.

03:45.360 --> 03:48.300
Now, sometimes for different reasons.

03:48.300 --> 03:55.680
You don't want to add additional elements, and you can also use a thing that's called fragments.

03:55.680 --> 04:03.180
So instead of using an actual HTML elements, you would use something like this which looks like an

04:03.180 --> 04:05.310
empty HTML tag.

04:05.310 --> 04:14.400
So this would also work just it wouldn't enclose the contents of this component JSX with an additional

04:14.400 --> 04:15.030
element.

04:15.030 --> 04:19.560
This is often important with styling with CSS.

04:20.340 --> 04:26.820
So JSX is a lot like HTML, though it is stricter.

04:26.820 --> 04:30.900
So for example, let me add an unordered list.

04:31.530 --> 04:42.420
So you start with ul element, then you add li, which can be task one and then task two below.

04:43.230 --> 04:48.450
So since we are using tailwind, that does not really render as a list.

04:48.450 --> 04:51.990
Anyway, we've got those HTML elements.

04:51.990 --> 04:56.010
Now inside HTML you can do something like this.

04:56.010 --> 05:00.390
You don't need to close those those elements explicitly.

05:00.390 --> 05:05.970
But when you save changes in JSX you've got an error, a fatal error.

05:05.970 --> 05:16.560
Because in JS JSX every element needs to be explicitly closed, whether by a closing tag like this or

05:16.560 --> 05:21.900
when you are inserting an image, then you need to self close it.

05:26.090 --> 05:30.470
Now another thing to remember is the element attribute syntax.

05:30.470 --> 05:34.160
So let me wrap this text inside a div element.

05:34.160 --> 05:38.150
So for the attribute names you would use CamelCase.

05:38.150 --> 05:45.500
So there is an onclick handler in HTML which looks like this in react or in JSX.

05:46.010 --> 05:49.580
This is CamelCase which looks like this.

05:50.390 --> 05:58.430
And I think that people often get wrong for some time when they start using react is how you use the

05:58.430 --> 06:05.480
class attribute of HTML, which lets you set some CSS classes on an element.

06:05.480 --> 06:14.000
So in JSX you can't use class attribute because it is a reserved word in JavaScript.

06:14.000 --> 06:17.030
And remember that's not HTML.

06:17.030 --> 06:22.550
This is JSX and it gets compiled to JavaScript.

06:22.550 --> 06:25.400
So we can't use this class keyword.

06:25.400 --> 06:26.210
Instead.

06:26.210 --> 06:30.830
To add a CSS class to an element, you use class name.

06:31.340 --> 06:37.730
So for example, from tailwind I can set a different background like this gray one.

06:42.100 --> 06:47.080
Let's actually change this background to a darker so we can see the text.

06:47.080 --> 06:51.400
And next up let's talk about the dynamic content in JSX.

06:51.850 --> 06:57.280
So let me define a variable called name with the value which would be my name.

06:57.280 --> 07:00.880
Now I'd like to render that right after hello.

07:00.880 --> 07:05.740
And to do that you will use curly braces and then type the variable name.

07:05.740 --> 07:07.270
As you see it got rendered.

07:07.270 --> 07:13.000
On the right is also a good example of something I've talked about before, which is the declarative

07:13.000 --> 07:17.680
rendering where you don't do any updates explicitly.

07:17.680 --> 07:25.510
You just tell react using JSX syntax, what needs to be rendered, what elements and what data needs

07:25.510 --> 07:31.750
to be on the UI and its job of react to make the necessary UI updates.

07:32.440 --> 07:38.530
Now finally, you would need to watch for all the errors which react tells you about.

07:38.530 --> 07:46.510
So typically, if you don't follow JSX rules, it will tell you that explicitly by showing you a huge

07:46.510 --> 07:53.080
error on the page that something is wrong and it will show you the place where something is wrong.

07:53.080 --> 07:59.500
So this way it's much easier to avoid mistakes and then fix the potential issues.

07:59.500 --> 08:05.410
So just watch closely all those errors that JSX gives you.
