WEBVTT

00:01.150 --> 00:01.480
All right.

00:01.480 --> 00:06.190
So at one point or another, you'd like your website to be interactive.

00:06.220 --> 00:10.840
Say you've got a button that when clicked you'd like something to happen.

00:10.840 --> 00:13.930
You would like to react to this event fast.

00:13.960 --> 00:18.280
Now we're going to talk about event handling in react.

00:20.270 --> 00:20.570
All right.

00:20.570 --> 00:26.390
So just make sure that the project is started by running npm run dev in the terminal.

00:26.390 --> 00:29.630
And I'm going to close this terminal window for now.

00:29.630 --> 00:36.260
So let's add a button to which we can add an event handler maybe right after the last card.

00:36.260 --> 00:40.370
So we'll just use the button element and say click me.

00:40.490 --> 00:46.280
So when I save the changes you should see the button right there though it doesn't really look like

00:46.280 --> 00:46.790
a button.

00:46.790 --> 00:52.970
And this is because the tailwind CSS is resetting all the styles of all elements.

00:52.970 --> 00:56.960
But indeed this is a button that can be clicked.

00:56.960 --> 01:00.410
But when I click on it, I'm doing it right now.

01:00.410 --> 01:01.670
Nothing happens.

01:01.670 --> 01:05.540
So we need to somehow add an event handler.

01:05.540 --> 01:14.270
So previously I've mentioned that the attributes in react use camel case and to add an event handler

01:14.270 --> 01:21.800
you will add an onclick attribute and every event handler is a JavaScript function.

01:22.070 --> 01:27.110
So we need to create a function that will be run when this button is being clicked.

01:27.960 --> 01:36.180
Now, the nice thing about event handling in react is that react wraps the native events or native event

01:36.180 --> 01:38.400
handling, or every browser.

01:38.400 --> 01:45.120
Thus, you don't really have to worry about the cross browser compatibility or differences in event

01:45.120 --> 01:45.930
handling.

01:46.080 --> 01:52.140
So when I save the changes right now, we see an error because we actually need to assign an expression.

01:52.140 --> 01:54.690
Here we need to add a function.

01:57.150 --> 02:03.240
So we can create an arrow function inline so directly inside the JSX.

02:03.750 --> 02:06.510
And this can just alert something.

02:06.630 --> 02:08.700
Let's say just hello.

02:08.880 --> 02:13.170
Now when I save changes we've got an error but a different one.

02:13.170 --> 02:19.830
This time it says that event handlers cannot be passed to client component props.

02:19.860 --> 02:24.450
Well, this sounds a little cryptic and that's not a react error.

02:24.450 --> 02:30.810
You need to remember that we are using Next.js and this comes from Next.js.

02:30.810 --> 02:38.940
So I think this is way too early to explain client and server components in next.

02:39.090 --> 02:44.370
So the only thing I'm going to say right now is at the beginning of the file, you need to write this

02:44.370 --> 02:49.890
use client and after you save changes it works again.

02:50.970 --> 02:52.890
So let's go back to events.

02:52.890 --> 02:59.790
Now when I click on this button you can see the alert with the text that I have specified.

03:00.030 --> 03:02.100
So this event handler works.

03:04.220 --> 03:11.660
So you can obviously write those inline event handlers, but most of the time the best convention is

03:11.660 --> 03:14.780
to define a function within component.

03:14.780 --> 03:21.350
So let me go to the top and define a function that will be called handleclick.

03:21.350 --> 03:25.550
It can also be an arrow function, but can also be a traditional function.

03:25.550 --> 03:30.050
There is no difference in this case and I would just say alert.

03:30.410 --> 03:31.220
Hello.

03:33.100 --> 03:40.450
And the convention in react is that you typically start the event handling function name with the word

03:40.450 --> 03:48.100
handle, and then use the event name or some more details if you have multiple event handling functions.

03:48.100 --> 03:55.420
And now we can pass this function name as an event handler to this button on click event.

03:55.420 --> 04:00.880
But watch out that you just need to pass the function name.

04:01.060 --> 04:03.400
Don't call this function inside here.

04:03.400 --> 04:05.500
I think that's a mistake.

04:05.500 --> 04:09.790
People do a lot and it is very common that instead.

04:10.450 --> 04:17.800
People call this function, which can cause an infinite loop, because this function will be called

04:17.800 --> 04:23.350
every time the React.component runs and every time it renders.

04:24.130 --> 04:27.190
So just make sure you don't call this function.

04:27.190 --> 04:29.890
Instead, you just pass the function name.

04:32.020 --> 04:37.870
Now, the last thing I like you to know is that in those event handling functions, you've got access

04:37.870 --> 04:39.850
to the actual event object.

04:39.850 --> 04:43.180
So that would be the first argument of such function.

04:43.360 --> 04:47.590
So if I now, uh, wrap this in braces.

04:49.380 --> 04:55.500
Like this, I can add additional console.log and log the actual event.

04:55.770 --> 04:58.500
So let me clear the console right here.

04:58.890 --> 05:02.520
And when I click on this button we see the alert.

05:02.520 --> 05:09.690
But also inside the console we see the event object which you can use to do many interesting things.

05:09.690 --> 05:16.260
For example, you can prevent the element default behavior by using E.preventdefault.

05:16.290 --> 05:17.970
This is useful in forms.

05:17.970 --> 05:24.480
For example, when the form is submitted, the default HTML behavior is to submit the form using the

05:24.480 --> 05:26.460
get method to the current URL.

05:26.460 --> 05:31.710
So when you are handling forms using JavaScript, you don't want this behavior.

05:31.710 --> 05:33.600
So that's useful.

05:33.600 --> 05:39.390
And additionally you can do many other things for example with event propagation.
