WEBVTT

00:00.620 --> 00:01.010
All right.

00:01.010 --> 00:08.690
So I think that the next obvious step for us should be to take a look at the created Next.js project

00:08.690 --> 00:09.650
structure.

00:09.650 --> 00:12.590
So there is a page called Project Structure.

00:12.590 --> 00:19.160
In the next docs, I'm gonna link to this page where you will have a pretty short description of every

00:19.160 --> 00:20.870
folder and file.

00:20.900 --> 00:28.940
I'd like to go more in depth, so let's quickly open our newly created project and then have a couple

00:28.970 --> 00:33.110
of words about every file and folder we can find there.

00:33.110 --> 00:42.710
So for me, the best way is to use the code dot command as a shortcut to open Visual Studio Code with

00:42.710 --> 00:44.210
our newly created project.

00:44.210 --> 00:48.560
So I just hit enter and this is opened VSCode.

00:48.560 --> 00:53.720
Now let me go over all those folders and files we see here.

00:54.890 --> 00:59.060
So let's begin with this dot next directory.

00:59.060 --> 01:05.120
So that's a folder automatically created and managed by next.

01:05.660 --> 01:09.590
So it's just the result of the next build process.

01:09.590 --> 01:14.960
You won't be modifying this directly, so let's just leave it as it is.

01:15.230 --> 01:18.650
Next up we've got the app folder.

01:18.680 --> 01:23.600
It's been introduced in Next.js 12 and later.

01:23.600 --> 01:33.170
And it just contains all the react components, all the pages layouts and different UI components that

01:33.170 --> 01:36.110
we are going to create for our application.

01:36.560 --> 01:47.510
Then we've got this node modules and that's a directory created by the node package manager like npm,

01:47.510 --> 01:50.870
which we are using in this course or yarn.

01:50.870 --> 02:00.320
And it contains all the dependencies of our project, which for example includes react or next.

02:00.890 --> 02:08.900
Now, you also don't modify the contents of this folder directly, because it's going to be recreated

02:08.900 --> 02:18.350
every single time when you run npm install based on the contents of this package-lock.json file, which

02:18.350 --> 02:23.930
lists all the libraries that need to be installed together with your project.

02:23.960 --> 02:31.760
Now, also, because this folder is typically huge, it's not checked in into source control.

02:31.760 --> 02:35.780
It's being ignored by adding an instruction inside the.

02:35.780 --> 02:37.310
Gitignore file.

02:37.310 --> 02:41.840
So it should never be checked in into your source control.

02:41.870 --> 02:45.620
Next up we've got the public folder.

02:45.680 --> 02:53.810
That's a special folder in next where you can place all the static assets like images, fonts and other

02:53.810 --> 02:54.830
files.

02:54.830 --> 03:03.650
And what's special about this folder is that all the files that you put in there will be available directly

03:03.650 --> 03:06.770
at the root of your domain.

03:07.280 --> 03:10.010
So let's see what this means.

03:11.990 --> 03:19.970
So let's quickly see that in practice I will jump to the terminal where I type npm run dev to start

03:19.970 --> 03:22.250
the next development server.

03:22.280 --> 03:26.930
Next I'm gonna visit this address localhost 3000.

03:26.960 --> 03:33.290
Inside the browser and I will have another look at the public directory.

03:33.290 --> 03:37.220
For example you've got a next dot SVG file in there.

03:37.220 --> 03:45.140
So let me try to get this file directly by typing the next SVG after our root domain.

03:45.230 --> 03:46.760
And there we have it.

03:46.760 --> 03:55.430
So I can see this image because as I've said everything inside this public folder is accessible publicly.

03:56.810 --> 03:57.110
All right.

03:57.110 --> 04:04.520
So now let's take a look at some of the files that we have here, starting with dot eslint rc dot JSON.

04:04.520 --> 04:12.560
So that's a configuration file for our tool called ESLint, which basically makes sure that your code

04:12.560 --> 04:19.310
quality is, uh, kept and that you are consistent with your coding style.

04:19.310 --> 04:26.900
And it comes with some pre-configured, sensible defaults, but you can obviously configure it to your

04:26.900 --> 04:28.340
own taste.

04:28.370 --> 04:32.990
Then we've got the dot git ignore file.

04:32.990 --> 04:40.970
And this is a file used by git version control system to just determine which files and directories

04:40.970 --> 04:43.670
are to be ignored when committing changes.

04:43.670 --> 04:48.800
For example, this node modules folder that I've mentioned previously.

04:49.520 --> 04:50.210
Rhys.

04:50.480 --> 04:58.190
Next up we've got the js config dot JSON or it would be also called tsconfig.json if you'd be using

04:58.220 --> 04:59.300
TypeScript.

04:59.300 --> 05:04.720
So this file configures the behavior of JavaScript inside your project.

05:05.650 --> 05:12.070
Now, the only setting that we currently have inside this file is an import path alias, which lets

05:12.070 --> 05:19.480
you import modules without having to use a relative path that is relative to the current file.

05:19.480 --> 05:26.710
Instead, you can use this absolute path using this at sign that will just point to the root directory

05:26.710 --> 05:27.760
of the project.

05:27.790 --> 05:30.400
More about this later on.

05:31.270 --> 05:37.900
Then we have the next Config.js, which is basically a configuration file of your next app.

05:39.130 --> 05:44.170
Then there is package.json and it has a couple of roles.

05:44.170 --> 05:52.810
So it defines all the dependencies that your project depends on the libraries that it's using which

05:52.840 --> 06:03.100
includes react, react, Dom or next and those inside this dependencies section are essential for your

06:03.100 --> 06:05.200
application to be able to run.

06:05.230 --> 06:10.870
Now there are also non-essential dependencies that are inside dev dependencies.

06:10.900 --> 06:17.620
They are only being used for development purposes or for testing purposes like this.

06:17.620 --> 06:19.990
Autoprefixer Postcss.

06:20.020 --> 06:28.750
Tailwind CSS is lint that checks the style and correctness of your code, so those inside dev dependencies

06:28.750 --> 06:31.120
are not essential for your app to run.

06:31.150 --> 06:34.390
Finally, we've got the scripts section.

06:34.390 --> 06:38.530
So this one you've already used the dev command.

06:38.620 --> 06:43.720
So this will start the local development server of Next.js.

06:44.200 --> 06:51.580
Then there is a build command which will just package your next application for deployment to a production

06:51.580 --> 06:52.330
server.

06:52.330 --> 06:57.520
So it will be optimized and all unnecessary things would be removed.

06:57.550 --> 07:02.680
Then the start command is used to start this build package.

07:02.680 --> 07:09.070
So if you'd like to start the application that was already built for deployment, you will do that using

07:09.070 --> 07:10.570
the start command.

07:10.570 --> 07:15.790
And then lint just runs all those code quality tools.

07:15.790 --> 07:24.100
So all of those scripts defined here are run by typing npm run followed by the script name.

07:24.130 --> 07:29.530
As I said, you can also add your own scripts into this section.

07:30.640 --> 07:37.720
Now then there is this package log JSON file and it's just automatically generated by npm.

07:37.720 --> 07:46.510
It basically is used to log the versions of all your project dependencies because as you see, you specify

07:46.510 --> 07:49.750
the version of every dependency next to it.

07:49.750 --> 07:57.940
So this file is being used to ensure that your application works consistently on all the environments

07:57.940 --> 08:05.230
and that the libraries will be installed not in the newest versions, but on those locked versions.

08:05.260 --> 08:12.340
Then we've got Postcss config, which is used to configure a Postcss.

08:12.370 --> 08:21.130
Postcss is a tool that transforms CSS with JavaScript, and this tool is being used by tailwind.

08:21.130 --> 08:28.810
So tailwind on the other hand, is a utility based CSS framework which is super popular.

08:28.810 --> 08:31.750
And we're going to use it inside this course.

08:31.750 --> 08:36.190
And tailwind just relies on Postcss.

08:38.260 --> 08:38.560
All right.

08:38.560 --> 08:42.580
So we've been talking a lot I think at this point you will need a short break.

08:42.580 --> 08:50.410
And then I will talk about the most important folder in this project structure, which is this app folder

08:50.410 --> 08:56.560
where all of our pages, layouts, components, UI components will go.

08:56.560 --> 08:59.590
So we're going to talk about it in the next video.
