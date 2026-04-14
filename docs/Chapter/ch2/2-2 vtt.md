WEBVTT

00:00.560 --> 00:01.040
All right.

00:01.040 --> 00:06.170
So let's learn how to create a brand new Next.js project.

00:06.200 --> 00:09.980
We are looking at the main page of Next.js.

00:10.010 --> 00:13.460
I'd like you to go to the documentation page.

00:13.460 --> 00:21.470
And generally I think that's a great habit to develop, to always have the documentation of whatever

00:21.470 --> 00:23.000
you are using open.

00:23.000 --> 00:30.470
And I will often refer to specific pages of the documentation throughout this course.

00:30.500 --> 00:39.680
Additionally, if you open the documentation then you always find the most up to date instructions there.

00:39.680 --> 00:45.500
So let's follow this installation page from the next docs.

00:46.970 --> 00:50.570
So first let's take a look at the system requirements.

00:50.570 --> 00:53.780
You need at least Node.js 18.

00:53.810 --> 00:59.390
So at this point I would assume you already have it, but it never hurts to check.

00:59.510 --> 01:06.980
So jump into the terminal and type node V to see what's your version of node.

01:07.010 --> 01:10.670
That's mine and it's just above.

01:10.670 --> 01:13.760
What's the minimum requirement to run next.

01:13.760 --> 01:17.390
So next can run on any operating system.

01:17.390 --> 01:18.980
So we are covered there.

01:18.980 --> 01:25.400
And now let's see how can we actually install or create a new Next.js app.

01:26.570 --> 01:34.130
Now in the docs you can read that the recommended way to start the next project is using the Create

01:34.160 --> 01:38.990
Next app, which should set up everything automatically for you.

01:38.990 --> 01:41.930
So let me open that in a new tab.

01:42.890 --> 01:48.590
So this is a CLI tool that will just ask you some questions.

01:48.590 --> 01:51.260
So some prompts will pop up.

01:51.260 --> 01:56.630
You will answer some questions and then it will generate the new next app.

01:56.630 --> 02:00.260
So this is a interactive CLI tool.

02:00.290 --> 02:08.270
But for those of you who don't know what that is, why do you write NPCs?

02:08.510 --> 02:10.130
Let me explain.

02:11.480 --> 02:13.580
So let's switch to the terminal.

02:13.610 --> 02:21.620
Now, every time you install Node.js on any machine, it ships with some additional command line tools.

02:21.620 --> 02:24.140
One of those is npm.

02:24.140 --> 02:29.420
If I type npm dash v, I should see the version of npm.

02:29.450 --> 02:33.980
Now we are not supposed to run npm but npm.

02:34.340 --> 02:37.820
So what's npx and what's npm?

02:37.850 --> 02:40.310
So npm is node package manager.

02:40.310 --> 02:48.140
It's used to install packages that you add to your project, or that you install globally on your system.

02:48.140 --> 02:57.290
So package is for example, Next.js itself or react is a package or any additional react library or

02:57.290 --> 03:04.220
JavaScript library is something that you will install to either globally run on your system, or to

03:04.250 --> 03:07.460
be part of your project that you are working on.

03:07.490 --> 03:10.520
Now NTP is different.

03:10.550 --> 03:19.610
It stands for node, package execute and it also always ships with node.

03:19.610 --> 03:26.900
So if I type NTP dash v you should also see the version of NPCs.

03:29.600 --> 03:38.600
So thanks to this NTP tool, we can run a specific package only once without having to install this

03:38.630 --> 03:40.190
on our machine.

03:40.190 --> 03:43.850
And well, it just runs once and that's it.

03:43.850 --> 03:45.380
You don't install anything.

03:45.380 --> 03:48.470
It doesn't leave any trace on your machine.

03:48.470 --> 03:52.790
So it's for running some one time scripts.

03:52.790 --> 04:00.070
And one of those is this create next app, which only job is to create a new next app for you.

04:00.070 --> 04:01.420
And that's it.

04:01.510 --> 04:09.820
Now, when you see this icon next to a code snippet or terminal command inside the Next.js docs, you

04:09.820 --> 04:14.050
can click on it to copy it quickly into the clipboard.

04:14.050 --> 04:22.900
So let's do that and jump back into the terminal and paste this command and just run it.

04:22.930 --> 04:28.630
Hit enter and then you will get a couple of prompts asking you some questions.

04:28.630 --> 04:33.400
So the first one is what is your project named.

04:33.400 --> 04:39.640
Let's call that next 14 blog and confirm with enter.

04:40.960 --> 04:45.160
So next up we are being asked whether we would like to use TypeScript.

04:45.160 --> 04:53.860
So normally I would say yes, but since I want this course to be easy to follow to all of you folks,

04:53.860 --> 04:59.080
even those that haven't used TypeScript before or don't know TypeScript.

04:59.110 --> 05:03.670
I will go with no design, which is the default.

05:03.700 --> 05:06.970
Next up would we like to use ES lint?

05:07.000 --> 05:14.620
Well, this is a library that will help us find some issues with our code before we run it.

05:14.620 --> 05:16.120
So obviously.

05:16.120 --> 05:16.750
Yes.

05:16.780 --> 05:17.380
Yes.

05:17.380 --> 05:24.490
We would like to use tailwind CSS because one of the nice things about next is it will pre-configure

05:24.520 --> 05:27.640
this CSS utility library for us.

05:27.640 --> 05:30.070
So we won't have to do that ourselves.

05:30.070 --> 05:31.660
So choose.

05:31.660 --> 05:32.530
Yes.

05:32.710 --> 05:38.050
Next we get a question whether we would like to use the src directory.

05:38.080 --> 05:43.810
Well this doesn't have any influence on the project whatsoever.

05:43.810 --> 05:46.060
It's just a matter of preference.

05:46.060 --> 05:54.070
Whether you would like to put all of your application logic inside this src folder.

05:54.070 --> 05:57.610
So as I've said, personal preference for me.

05:57.610 --> 05:58.840
It's a no.

05:59.860 --> 06:02.290
Next up, whether you'd like to use.

06:02.320 --> 06:03.310
Up router.

06:03.310 --> 06:06.250
So obviously yes.

06:07.510 --> 06:11.470
And we don't need to customize the import.

06:11.500 --> 06:11.980
Alias.

06:11.980 --> 06:14.710
So stick with the default which is no.

06:14.710 --> 06:18.640
And now we just need to wait for next to.

06:18.670 --> 06:23.050
Install all the libraries and it will tell us when it's ready.

06:29.740 --> 06:30.190
All right.

06:30.190 --> 06:31.180
So our.

06:31.210 --> 06:32.530
App is created.

06:32.530 --> 06:36.190
Let's now jump into the folder.

06:36.190 --> 06:39.370
That's next 14 blog.

06:41.110 --> 06:44.110
Now I'd like you to start the Next.js.

06:44.140 --> 06:49.570
Development server by running the npm run dev command.

06:49.600 --> 06:52.780
Hit enter and wait for it to boot up.

06:52.780 --> 07:01.390
This starts the local next development server, and it will display the URL under which our next app

07:01.390 --> 07:03.280
is available locally.

07:03.280 --> 07:09.070
I'd like you to copy this URL, jump into the browser and paste it.

07:10.240 --> 07:17.680
Then confirm with enter and you should see a Next.js Welcome page which confirms that everything was

07:17.680 --> 07:23.530
installed properly and next now works locally so we can work on our project.

07:24.970 --> 07:25.300
All right.

07:25.330 --> 07:31.690
Now to stop this development server you will hit control C on your keyboard.

07:32.020 --> 07:35.260
So this stops the Next.js development server.

07:35.260 --> 07:36.850
And that's it for this video.

07:36.850 --> 07:42.040
So congratulations on creating your first Next.js project.

07:42.070 --> 07:47.350
Now next up we're gonna discuss the Next.js project structure.

07:47.350 --> 07:54.610
And also I will go over all the available commands like this npm run dev.
