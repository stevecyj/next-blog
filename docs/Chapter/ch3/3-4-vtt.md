WEBVTT

00:00.290 --> 00:10.850
Now this JSX syntax, together with the JavaScript logic and closed in a JavaScript function makes a

00:10.850 --> 00:12.680
react component.

00:12.680 --> 00:21.500
So react components are fundamental for building the user interfaces, and essentially every one of

00:21.500 --> 00:25.940
those components is just a reusable UI element.

00:26.600 --> 00:34.490
So the react component is a JavaScript function that returns JSX.

00:35.090 --> 00:41.240
And those components, they combine the markup CSS and the JavaScript.

00:42.110 --> 00:47.600
Now, when you give the name to your components, they should start with a capital letter.

00:48.930 --> 00:56.250
Now this export default that you see here is exporting this component function from this file.

00:56.670 --> 01:05.550
Now the best convention in react and also in next is to create one react component per file and then

01:05.550 --> 01:09.540
export it so it can be imported and used elsewhere.

01:09.540 --> 01:14.670
So this really helps to make your code organized and manageable.

01:14.760 --> 01:23.730
And having said that, I'm going to now add some more components into this file just for the demonstration

01:23.730 --> 01:24.810
purposes.

01:26.370 --> 01:26.700
All right.

01:26.700 --> 01:31.080
So let's create a new component directly inside this file.

01:31.080 --> 01:33.780
So every component is a function.

01:33.780 --> 01:36.870
So let me define a function called card.

01:37.500 --> 01:40.290
It won't accept any parameters for now.

01:40.290 --> 01:43.530
And as said every component returns JSX.

01:44.040 --> 01:55.470
So let me return the JSX inside the brackets I want to return a div element that would just say card

01:55.470 --> 01:56.670
component.

01:57.150 --> 02:00.720
Maybe just this text for now and let me style that.

02:00.720 --> 02:03.060
So we use className.

02:03.060 --> 02:05.160
As we've learned, we can't use class.

02:05.160 --> 02:12.030
It's a reserved keyword, and I'm going to use some tailwind classes to style this card element.

02:12.030 --> 02:19.380
So I want this to have a border to be rounded medium to have border gray.

02:21.540 --> 02:23.340
Maybe 600.

02:23.340 --> 02:26.610
And to have padding of size four.

02:27.600 --> 02:35.610
Now I'm gonna modify this original component by removing this background, and instead I'm gonna add

02:35.610 --> 02:38.700
huge padding of size 20.

02:38.700 --> 02:41.460
So you see how our page changed.

02:41.460 --> 02:43.830
Now everything is more centered.

02:43.830 --> 02:49.470
And next up we're gonna use this new card component that we have just created.

02:50.680 --> 02:55.540
So first let me wrap this text inside a div element.

02:55.540 --> 02:58.630
And let's see how do we use components.

02:58.630 --> 03:05.890
So we just use the component using the component name as it would be an HTML element.

03:05.890 --> 03:11.410
So I do card and I need to close this element for some separation.

03:11.410 --> 03:16.600
Let's add a space y for class to this parent div element.

03:16.600 --> 03:25.960
And now let me copy paste this card couple of times so we can prove that those components are reusable

03:25.960 --> 03:27.310
UI elements.

03:27.670 --> 03:30.700
So I didn't have to write all this markup.

03:30.700 --> 03:35.950
Again I've defined some CSS classes and I display some content.

03:35.950 --> 03:42.280
And then I can reuse this everywhere easily by just using this card component.

03:44.540 --> 03:48.710
All right, so this is nice, though this card isn't really useful.

03:48.710 --> 03:54.410
You always display card component the same text in every single one of those cards.

03:54.410 --> 03:58.820
And maybe you'd like to put some custom text inside those cards.

03:59.030 --> 04:00.080
How can we do that?

04:00.080 --> 04:06.050
Well, to pass data to the so-called child component, which card is.

04:06.050 --> 04:12.830
In this case, you will use a thing called props, which is a shortcut for properties.

04:12.830 --> 04:17.870
So let's define an argument on this function called props.

04:18.050 --> 04:24.500
And now I can pass data to card using HTML attributes.

04:24.860 --> 04:28.850
So let me create a prop called text.

04:28.850 --> 04:35.810
And I'm going to say this is being passed from the parent.

04:37.120 --> 04:37.660
All right.

04:37.660 --> 04:43.810
So now this card component can receive this data and it can render it.

04:44.170 --> 04:46.330
So I use curly braces.

04:46.330 --> 04:54.520
And the props should now have the text property, the same one that I've set to this card component

04:54.520 --> 04:56.200
using an attribute.

04:56.500 --> 05:03.250
And as you see and as expected this is now rendered within this card component.

05:03.670 --> 05:04.270
Okay.

05:04.270 --> 05:06.220
So this is much better.

05:06.220 --> 05:11.530
We can now do something more interesting with this card component.

05:11.530 --> 05:20.110
Yet you immediately probably felt that it would be even more useful if I could pass some actual markup

05:20.110 --> 05:20.620
in there.

05:20.620 --> 05:28.750
Let's say I would like to add some buttons, maybe some other styles, maybe images inside those cards,

05:28.750 --> 05:34.810
and this looks pretty hard to do passing it through an attribute.

05:34.810 --> 05:39.640
And for that we will need to talk more about the props.

05:41.590 --> 05:46.090
So next let's talk about the props in detail.
