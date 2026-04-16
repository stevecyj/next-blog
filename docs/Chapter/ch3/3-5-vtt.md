WEBVTT

00:00.200 --> 00:08.780
So props are being passed from the parent component like home to a child component like card and props

00:08.780 --> 00:15.290
are used to customize the behavior and appearance of the child component.

00:15.290 --> 00:22.280
And they are similar to HTML attributes, but they also can include JavaScript.

00:22.280 --> 00:28.880
So you are not limited to passing strings like in HTML attributes.

00:28.880 --> 00:37.760
You can also pass a JavaScript expression by surrounding it with curly braces, so you can also pass

00:37.760 --> 00:39.380
the text this way.

00:41.710 --> 00:44.380
As you can see, this also works.

00:45.430 --> 00:53.110
Now those props in the child component, they are being accessed by this first argument of a component,

00:53.110 --> 00:55.930
which is typically called props.

00:55.930 --> 01:03.460
And this is an object which has the properties with everything that you pass using this attribute like

01:03.460 --> 01:04.450
syntax.

01:04.660 --> 01:13.270
Now you can also use destructuring in here because a set props is an object, so you can destructure

01:13.270 --> 01:18.910
it to get the specific properties from this object like the text.

01:18.910 --> 01:26.260
So now instead of using this props and prepend props with every single time you'd like to access some

01:26.260 --> 01:30.310
data, you can immediately use text as a variable.

01:30.310 --> 01:32.650
As you see, everything still works.

01:34.360 --> 01:40.330
You can set the default value of a prop by setting the default argument value.

01:40.360 --> 01:46.720
So let's say for text, I would set it to nothing to say.

01:48.100 --> 01:52.480
And those three last cards display this default text.

01:54.340 --> 02:02.860
Now, as said previously, you might prefer to actually pass some content inside this card element like

02:02.860 --> 02:05.650
you would normally do in HTML.

02:05.800 --> 02:08.290
So this is a good example.

02:08.290 --> 02:15.250
So instead of passing this text hello through an attribute to a div element, you just put it between

02:15.250 --> 02:18.130
opening and closing div element.

02:18.160 --> 02:21.040
Now this is also possible with JSX.

02:21.730 --> 02:28.210
So you will define a special prop called children.

02:29.020 --> 02:32.980
And then you will just render it whenever you'd like it rendered.

02:32.980 --> 02:38.440
And that way you can pass JSX to this component.

02:39.500 --> 02:40.820
So let's do that.

02:40.820 --> 02:44.930
Let's replace this text prop.

02:46.250 --> 02:55.550
And then everything that you pass within opening and closing, uh, element of your component will be

02:55.550 --> 02:59.630
passed to this children prop.

02:59.630 --> 03:02.120
And as you see this is being rendered here.

03:02.120 --> 03:06.440
So if I now update this second component.

03:09.290 --> 03:12.680
Now this text is also displayed within the card.

03:12.710 --> 03:22.490
Now, what's even cooler is that you can compose the components so you can render component within a

03:22.490 --> 03:23.450
component.

03:24.260 --> 03:26.360
So let me show you an example.

03:26.690 --> 03:32.000
I can use a card component inside another card component.

03:32.000 --> 03:35.870
Let me put nested text inside this one.

03:36.390 --> 03:40.290
And this card renders inside another card.

03:42.080 --> 03:48.260
Now, the last thing that I need you to know about props is that props are read only and they should

03:48.260 --> 03:51.170
never be modified within a component.

03:51.170 --> 03:58.160
So the data always needs to flow down from the parent component into child components.

03:58.550 --> 04:06.860
And there are ways for child components to tell parents that something has changed and needs to be updated,

04:06.860 --> 04:11.240
but never by modifying the past props directly.
