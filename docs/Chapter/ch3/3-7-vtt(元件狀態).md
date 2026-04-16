WEBVTT

00:00.410 --> 00:00.770
All right.

00:00.770 --> 00:04.160
So now let's talk about the component state.

00:04.160 --> 00:10.220
And I will try to explain the component state by relying on an example.

00:10.220 --> 00:17.240
So in my example inside this home component we've got this button which doesn't really look like a button

00:17.240 --> 00:18.650
but it is a button.

00:18.860 --> 00:24.530
And I'd like this button to have a different label once I click it.

00:24.530 --> 00:32.150
So the default might be called show, but once this button is clicked, I'd like the label on the button

00:32.150 --> 00:34.190
change to hide.

00:34.790 --> 00:40.400
So let's first see the naive way, which you might think would work, but it won't.

00:40.400 --> 00:42.320
But let's try that.

00:43.730 --> 00:50.810
So you might want to define a variable using let, which is important because if you define it using

00:50.810 --> 00:53.900
const, this variable can't be reassigned.

00:53.900 --> 00:59.750
And we would like to change the value of the variable and call this label.

00:59.750 --> 01:01.910
And initialize it with the value.

01:01.940 --> 01:08.330
So now it's fine to use this variable inside JSX like that.

01:08.330 --> 01:13.730
So I'm going to replace the current label with the value of the label variable.

01:13.730 --> 01:16.490
And as you see this works.

01:17.390 --> 01:24.710
Now let's change this event handler so that it will try to change the label when the button is being

01:24.710 --> 01:25.430
clicked.

01:25.670 --> 01:35.150
So let me replace this line with alert to modify the label to the text height, and then click on the

01:35.150 --> 01:35.960
button.

01:35.960 --> 01:39.860
So you see that the text is still the same.

01:39.860 --> 01:47.000
It's still show, even though when you take a look at the console, you see that the event was logged,

01:47.060 --> 01:50.270
which means that this handler is working.

01:50.270 --> 01:55.430
It was definitely called and the label was modified to be hide.

01:55.430 --> 01:58.670
Yet this is not reflected in the UI.

01:58.700 --> 01:59.930
Why is that?

02:00.410 --> 02:05.120
So to help us understand what's happening, let's add console logs.

02:05.420 --> 02:10.190
So console log right after the label definition the text render.

02:10.820 --> 02:17.780
And in this event handler, let's remove the argument and instead let's console log text event.

02:18.600 --> 02:23.700
Now when I save the changes, you immediately see the render being outputted.

02:23.730 --> 02:31.950
But if I click on this show button we see event, yet we don't see the text render.

02:31.950 --> 02:38.760
And this means that the component wasn't rerendered as the effect of clicking this button.

02:38.760 --> 02:47.460
So nothing triggered react to try and rerender the UI to figure out if there are any changes in the

02:47.460 --> 02:48.060
UI.

02:48.060 --> 02:53.280
So this means that react just didn't know about any changes.

02:53.280 --> 03:02.970
So the fact is that this label does just a variable and react doesn't keep track of this variable.

03:02.970 --> 03:07.710
So you've changed that variable in this event handler function.

03:07.710 --> 03:09.960
But this meant nothing to react.

03:09.960 --> 03:11.340
It was ignored.

03:11.400 --> 03:19.980
And for something to actually happen, you need to explicitly tell react about the component state.

03:20.710 --> 03:30.610
So the state is being kept between component rerenders, but also the change to the state which react

03:30.610 --> 03:35.680
actually tracks can trigger the react component rerender.

03:35.680 --> 03:42.490
So then it will know that it needs to update the label on that button.

03:42.670 --> 03:47.410
So to use state we need to learn about hooks.

03:48.700 --> 03:56.440
So hooks are functions, special functions in react that let you, as the name suggests, hook into

03:56.440 --> 03:57.760
certain react features.

03:57.760 --> 04:01.150
One of those is keeping the state of a component.

04:01.750 --> 04:06.550
Now the hook for keeping the component state is called use state.

04:06.850 --> 04:08.860
Let's use this hook.

04:09.010 --> 04:14.830
So we start with const array syntax and we call use state.

04:15.460 --> 04:20.590
Keep in mind that you will have to add an import statement for use state.

04:20.620 --> 04:22.690
Import it from react.

04:22.720 --> 04:26.050
Now why we use the array syntax.

04:26.290 --> 04:34.840
Well this is a array destructuring operator because use state returns an array where the first element

04:34.840 --> 04:37.870
is the variable you'd like react to.

04:37.870 --> 04:39.100
Keep track of.

04:39.100 --> 04:41.110
Let's call this label.

04:41.260 --> 04:45.850
And the second element of the returned array is a function.

04:45.850 --> 04:54.220
This special function should always be used by you to let react know that you want this label state

04:54.220 --> 04:55.150
modified.

04:55.150 --> 04:58.060
So let's call this set label.

04:58.060 --> 05:04.360
By the way, you just come up with the names of this state variable and the function.

05:04.360 --> 05:06.700
You can use any name you like.

05:06.700 --> 05:10.570
It is just a convention that you call this variable.

05:10.570 --> 05:12.160
However it needs to be called.

05:12.160 --> 05:18.460
And this setting function is called set followed by CamelCase variable name.

05:18.460 --> 05:21.400
Now obviously we now have a name conflict.

05:21.400 --> 05:25.450
So I need to remove this variable definition.

05:25.540 --> 05:32.470
And as said you don't modify this label explicitly by assigning to it.

05:32.470 --> 05:37.480
Instead you call the function the set label function.

05:40.660 --> 05:47.260
Now our button seems to have disappeared, and this is because the label does not have an initial value.

05:47.260 --> 05:52.180
So to set the initial value to the state, you just pass it to the use state function.

05:52.180 --> 05:54.850
So let's pass it as show.

05:56.810 --> 06:04.400
Now, after I save the changes, we see that the button is back again and when I click on it, it now

06:04.430 --> 06:07.220
magically changes to hide.

06:07.580 --> 06:09.350
So now it works.

06:09.350 --> 06:18.080
Now the component keeps the state and even though we see there are multiple rerenders, it's not being

06:18.080 --> 06:24.380
reset to the original state to the initial show state, it is being rendered as hide.

06:24.860 --> 06:29.600
So this is how you keep the state in a react component.

06:30.660 --> 06:34.890
All right, so now let's get rid of those console logs.

06:37.360 --> 06:44.980
And also, what you need to know about the hooks is that it's always best to call all the hooks that

06:44.980 --> 06:52.360
you are going to be using at the top level of the components, so never call them inside loops, conditions,

06:52.360 --> 06:54.340
or even nested functions.

06:54.340 --> 07:01.030
So hooks should always be called first at the top level of the component function.

07:01.660 --> 07:01.930
All right.

07:01.930 --> 07:04.480
So at the end let's remove this argument.

07:04.480 --> 07:07.180
And then let's actually toggle the label.

07:07.180 --> 07:13.270
So instead of always setting it to hide let's first check what's the current value of label.

07:13.270 --> 07:18.580
So if that's show let's change it to hide.

07:19.210 --> 07:21.670
But if it's already hide change it.

07:21.670 --> 07:23.170
Back to show.

07:23.170 --> 07:28.660
Now when I save the changes and I click on this button, you can see how I can toggle the label on the

07:28.660 --> 07:29.980
button by clicking on it.

07:30.400 --> 07:38.200
So as a recap, you don't use JavaScript variables for state, you can still use them inside component,

07:38.200 --> 07:44.680
but the changes to those variables won't trigger the rerender of a component.

07:44.680 --> 07:51.700
Instead, to keep the state between Rerenders and also to trigger the component rerender when the state

07:51.700 --> 07:55.450
changes, you use this use state hook.
