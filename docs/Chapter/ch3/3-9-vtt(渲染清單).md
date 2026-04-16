WEBVTT

00:00.230 --> 00:00.680
Okay.

00:00.680 --> 00:06.680
So next up let's talk about how to render a list of elements.

00:07.010 --> 00:13.130
So in our simple example here we've just used multiple card components.

00:13.130 --> 00:16.370
And in some places we put something inside.

00:16.370 --> 00:18.410
In others we don't.

00:18.800 --> 00:28.040
But in real life you typically render a list from some kind of data, which typically is just an array

00:28.040 --> 00:31.760
of elements that you would have to render.

00:32.060 --> 00:37.670
So first let me show you an example of how this data might look like.

00:37.670 --> 00:43.670
We are also going to start immediately with using use state for this purpose.

00:44.870 --> 00:51.500
So you might get names and uh sorry and set names.

00:51.500 --> 00:58.460
So this is going to be an array that we will initialize with some random names.

00:58.460 --> 01:03.080
Maybe Pyotr John Terry.

01:03.530 --> 01:08.150
Now we want to display this list of names.

01:08.660 --> 01:10.430
Um, I've made a mistake.

01:10.430 --> 01:10.670
Yes.

01:10.670 --> 01:11.570
Not the cost.

01:11.570 --> 01:13.520
It's const.

01:14.540 --> 01:22.820
And now we would like to display every single name in a separate card instead of those random bits.

01:23.150 --> 01:25.070
So let's see, how can we do that?

01:26.740 --> 01:28.990
So let's replace this code.

01:29.510 --> 01:36.530
And to render the list of elements, you will just use the array map method.

01:36.890 --> 01:41.150
So we have the array that's called names.

01:42.440 --> 01:51.530
Names has this map function, and we can pass an arrow function to convert every single name from that

01:51.530 --> 01:53.090
array into JSX.

01:55.050 --> 02:04.380
So this would be name then an arrow function, and we turn that into a card inside which we display

02:04.380 --> 02:05.580
the person name.

02:05.580 --> 02:14.430
When I save the changes you can see that this works out of the box though we have an arrow there.

02:14.430 --> 02:25.200
So for the performance reasons, when you render lists in react, every component or HTML element doesn't

02:25.200 --> 02:33.240
matter that you render as part of the list, it needs to have a unique key, at least the top level

02:33.240 --> 02:37.350
element of every every element from the list that you render.

02:37.350 --> 02:42.180
Not every single component, because you might nest some components.

02:42.180 --> 02:45.780
So you need to add a unique key in here.

02:45.780 --> 02:53.100
And well we can use name for that because at this point this is unique.

02:53.100 --> 02:59.550
But the best practice is to use something that you can make sure will be unique.

02:59.550 --> 03:03.720
And in our case names can repeat.

03:03.900 --> 03:11.880
So if you if you will add another person to that list and it happens to be another John or Terry, you

03:11.880 --> 03:13.740
will have the same issue again.

03:13.740 --> 03:22.740
So when rendering arrays and when using the map method of arrays, the first argument is the actual

03:22.740 --> 03:23.280
value.

03:23.280 --> 03:24.540
So name.

03:24.540 --> 03:30.270
But the second one would be the index of that element in the array.

03:30.270 --> 03:36.210
So the best way is to just use an index from the array.

03:37.620 --> 03:37.950
All right.

03:37.950 --> 03:46.410
So when talking about rendering the list of elements I can't skip talking about how do you modify an

03:46.410 --> 03:48.900
array of elements in react.

03:48.900 --> 03:52.320
So it also triggers a UI update.

03:52.320 --> 03:55.140
We've got this set names method here.

03:55.140 --> 03:57.600
So let's do an example.

03:57.600 --> 04:00.510
Let's add another button in here.

04:00.960 --> 04:03.060
So we add a button.

04:03.060 --> 04:05.010
Let's call this add.

04:05.040 --> 04:11.100
This will add just a random um element to this array.

04:11.310 --> 04:14.220
Let me put that into a div.

04:14.220 --> 04:18.240
So we've got some separation between those buttons.

04:18.660 --> 04:26.100
So let's make this a flex container with some space between those elements that's horizontal.

04:26.520 --> 04:26.820
All right.

04:26.850 --> 04:30.870
Now let's add an onclick handler.

04:31.500 --> 04:34.890
And let me call that handle add.

04:36.030 --> 04:37.770
So this doesn't exist.

04:37.770 --> 04:40.200
That's why we've got an error.

04:40.200 --> 04:46.680
And I'm going to add this handler here handle add.

04:47.460 --> 04:50.040
That's an arrow function.

04:50.580 --> 04:59.250
And to modify the names which is an array you won't be using the push method which is the way in JavaScript

04:59.250 --> 05:02.430
to add something to the end of array.

05:02.430 --> 05:09.240
Instead, you need to always manage state by using this setter function.

05:09.240 --> 05:15.240
So to add something to this array you have to use set names.

05:15.690 --> 05:22.800
And the trick is to just create another array, which you do by just using square brackets.

05:22.800 --> 05:30.630
And then you use the spread operator to copy all the items from this original names array into the new

05:30.630 --> 05:34.740
array, and at the end you add a new element.

05:34.740 --> 05:40.020
Let's just use some static text like new element.

05:43.560 --> 05:46.590
Then save the changes and let's try that out.

05:46.590 --> 05:56.190
So hiding and showing should still work and adding new elements also works and triggers the UI update.
