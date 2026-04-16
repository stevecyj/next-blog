WEBVTT

00:00.370 --> 00:05.140
So now we're gonna learn about the conditional rendering in react.

00:05.170 --> 00:08.020
This is a pretty straightforward concept.

00:08.410 --> 00:16.840
So you just want certain parts of your JSX in your component rendered when the specific condition is

00:16.840 --> 00:17.500
true.

00:17.530 --> 00:26.830
So if we take a look at our example, I see two cases where we might introduce conditional rendering.

00:26.920 --> 00:35.920
So instead of keeping the state of the label, instead we might use a different state variable called

00:35.920 --> 00:37.330
is visible.

00:37.330 --> 00:42.610
And then we're gonna based on this is visible variable.

00:42.610 --> 00:49.540
We are gonna conditionally render the label on the button to be either show or hide.

00:49.780 --> 00:55.690
And then maybe we can hide or show this whole list of cards.

00:56.260 --> 01:02.290
So let's see how can we do that and what options do we have for conditional rendering?

01:03.040 --> 01:05.050
Let's move step by step.

01:05.050 --> 01:11.230
The first step would be to rename this label variable to is visible.

01:12.110 --> 01:16.550
And the setter also needs to be renamed to set is.

01:18.040 --> 01:19.030
Feasible.

01:19.240 --> 01:22.600
The default state for that would be true.

01:22.600 --> 01:26.140
So by default we want the list to be visible.

01:26.140 --> 01:27.760
It can be hidden.

01:28.240 --> 01:35.590
Now in this Handleclick handler we now have to call our new method or sorry.

01:35.590 --> 01:39.370
The new function which is set is visible.

01:39.370 --> 01:45.280
And this would just toggle the value of is visible.

01:45.820 --> 01:53.200
So don't save the changes just yet because now we're gonna do our first conditional rendering.

01:53.200 --> 02:03.190
So now instead of keeping the label as a state of the component, we only keep if the user wants the

02:03.190 --> 02:05.410
data displayed or not.

02:05.410 --> 02:14.020
So the first way to do conditional rendering is using the so-called ternary operator.

02:14.020 --> 02:19.300
So we begin with the the curly braces.

02:19.300 --> 02:26.500
And then we just check the value of the variable which is is visible.

02:27.370 --> 02:29.890
And the ternary operator is question mark.

02:29.890 --> 02:37.330
And the first value would be returned if the condition is true, and the other one the second one when

02:37.330 --> 02:38.440
it is false.

02:38.440 --> 02:41.380
So when is visible is true.

02:41.410 --> 02:49.270
We want to display the text show sorry the text hide, so if it's already visible, we give an option

02:49.270 --> 02:50.500
to hide it.

02:50.500 --> 02:54.610
But if it's not visible, we display the text show.

02:54.760 --> 02:59.590
Now you can save the changes and let's test that.

03:00.700 --> 03:02.380
So it toggles properly.

03:02.380 --> 03:06.790
So our first case of conditional rendering is covered.

03:08.500 --> 03:15.610
Next up, we wanted to render this list of cards only if is visible is true.

03:15.910 --> 03:18.520
Otherwise we just render nothing.

03:19.180 --> 03:25.870
So another way to do conditional rendering is by using the logical and operator.

03:26.260 --> 03:31.240
So in this case we also surround that with the curly braces.

03:31.240 --> 03:34.810
And we do is visible.

03:34.810 --> 03:37.990
And then you use the and operator.

03:38.020 --> 03:45.190
Now since we have multiple HTML elements let's wrap them inside fragment.

03:45.190 --> 03:51.160
So this empty tag and then paste the content.

03:52.600 --> 03:56.230
Now let me save the changes and try that out.

03:56.860 --> 03:57.220
Okay.

03:57.220 --> 03:58.900
So this looks fine.

03:59.530 --> 03:59.920
Right.

03:59.920 --> 04:02.500
So let me show you another thing that you can do.

04:02.530 --> 04:06.190
You can actually set variables with JSX.

04:06.430 --> 04:10.210
So we can assign JSX to variables.

04:11.020 --> 04:14.530
Let me cut that from the content.

04:14.530 --> 04:25.480
And instead let's create a variable const cards and set it to this conditionally rendered JSX.

04:26.350 --> 04:33.220
And now in this place I will just render the value of the cards variable like that.

04:34.750 --> 04:36.700
Confirm that it still works.
