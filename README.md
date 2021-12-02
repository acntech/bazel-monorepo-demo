# Mono repository

A monorepo is a unified code base for multiple projects sharing dependencies, libraries etc. It is an architectural pattern where a single repository will contain all of the code for a given project. In other words, you can have several apps in one repo. Or you can also have a single repo that contains several different modules of a complex application.

## Monorepo vs. polyrepo
Monorepos are often great for microservices because they stay integrated and share infrastructure in the code base. A multirepo is a decentralized and bottom-up way of keeping your code while monorepos organizes as centralized and top-down. Polyrepos often require a lot publishing and versioning handling of the repositories / services. If you commit changes in a repo in a polyrepo ecosystem, other repositories dependant on that repo will also potentially be affected by that change. Therefore, you have to verify that the other dependant repositories still works with the changes you introduced to the code base. However, you could also keep the dependant repositories pinned to the old version of the repo you commited changes to, avoiding the integration verification. This will kick the integration problem down the road but will have to be solved at a later time. Then the integration problem will have to be solved by someone else without context or by you when you have forgotten all about it. You have no publishing / versioning in a monorepo, the consumers are all in the same repo. Thus, integration crashes are imminent and must be adressed immediately. 

### Monorepo advantages
 * __Shared configs__ - You can have a single source of configurations for the whole projects. This makes it easier to manage config.
 * __Code reuse__ - Eaisier to share and reuse code across the project.
 * __Transparency__ - Code visibility to every project for everyone involved.
 * __Atomic changes__ - Chagnes are reflected in all the packages, thus making development quicker.
 * __Unified Git history__ - All version history is collected in onw repo.

 ### Monorepo disadvantages
 * __Unable to restrict access__ - Every member has access to all the code.
 * __Long build times__ - The build time can be much longer when you have all the code in one place.
 * __Git performance__ - Since a lot of developers will commit chagnes in one place, teh Git performance can become slower as the history deepens. 
 
## Companies using monorepo
Lots of top companies use monorepo. Some of them include:
 * Google
 * Facebook
 * Microsoft
 * Uber
 * Airbnb
 * Twitter

# Bazel build and test tool
Bazel is an open-source build and test tool similar to Maven. It uses a human-readable, high-level build language. Bazel supports projects in multiple languages and builds outputs for multiple platforms. Bazel supports large codebases across multiple repositories, and large numbers of users. The ultimate goal of Bazel is to speed things up when we work with a monorepo which grows in code base size and number of contributors.  Bazel is used by and continuously developed and improved by Google and has a large community base. It is a very useful tool when you have many files and dependencies.

[See Bazel documentation](https://docs.bazel.build/versions/main/bazel-overview.html)

## Bazel concept and terminology
Before you can build a project, you need to set up its workspace. A workspace is a directory that holds your project’s source files and Bazel’s build outputs. It also contains files that Bazel recognizes as special:

* The WORKSPACE file, which identifies the directory and its contents as a Bazel workspace and lives at the root of the project’s directory structure,
* One or more BUILD files, which tell Bazel how to build different parts of the project. (A directory within the workspace that contains a BUILD file is a package. You will learn about packages later in this tutorial.)
To designate a directory as a Bazel workspace, create an empty file named WORKSPACE in that directory.


### Target
A BUILD file contains several different types of instructions for Bazel. The most important type is the build rule, which tells Bazel how to build the desired outputs, such as executable binaries or libraries. Each instance of a build rule in the BUILD file is called a target and points to a specific set of source files and dependencies. A target can also point to other targets.

## Bazel benefits

* __High-level build language.__ Bazel uses an abstract, human-readable language to describe the build properties of your project at a high semantical level. Unlike other tools, Bazel operates on the concepts of libraries, binaries, scripts, and data sets, shielding you from the complexity of writing individual calls to tools such as compilers and linkers.

* __Bazel is fast and reliable.__ Bazel caches all previously done work and tracks changes to both file content and build commands. This way, Bazel knows when something needs to be rebuilt, and rebuilds only that. To further speed up your builds, you can set up your project to build in a highly parallel and incremental fashion.

* __Bazel is multi-platform.__ Bazel runs on Linux, macOS, and Windows. Bazel can build binaries and deployable packages for multiple platforms, including desktop, server, and mobile, from the same project.

* __Bazel scales.__ Bazel maintains agility while handling builds with 100k+ source files. It works with multiple repositories and user bases in the tens of thousands.

* __Bazel is extensible.__ Many languages are supported, and you can extend Bazel to support any other language or framework.


# Build project commands

As a side notes, all Bazel commands are run from the WORKSPACE folder, which is considered the root. In this project we have implemented several sup-project with different languages.

## Java
### Build & Run
To build the ProjectRunner run

`bazel build //java:ProjectRunner`

With Bazel you can split the project up into multiple targets and packages allows Bazel for fast incremental builds. In other words, only rebuild what is changed and making it possible to build multiple parts of the project at once. With this configuration Bazel first builds the greeter library, then the ProjectRunner binary. The deps attribute in java_binary tells Bazel that the greeter library is required to build the ProjectRunner binary. If you now modify ProjectRunner.java and rebuild the project, Bazel only recompiles that file. 

To run the ProjectRunner run

`bazel-bin/java/ProjectRunner`
### Dependency graph

The dependency graph of the ProjectRunner java class can be first generated with

`bazel query  --notool_deps --noimplicit_deps "deps(//java:ProjectRunner)" --output graph`

Then visualized by copying the string output to http://www.webgraphviz.com/. we see the dependency graph and why projectRunner only is rebuilt if modified.
You’ve now built the project with two targets. The ProjectRunner target builds two source files and depends on one other target (:greeter), which builds one additional source file.

### Multiple BUILD packages

Let’s now split the project into multiple packages. If you take a look at the src/main/java/com/example/cmdline directory, you can see that it also contains a BUILD file, plus some source files. Therefore, to Bazel, the workspace now contains two packages, //src/main/java/com/example/cmdline and //, since there is a BUILD file at the root of the workspace.

However, for the build to succeed, you must explicitly give the runner target in //src/main/java/com/example/cmdline/BUILD visibility to targets in //BUILD using the visibility attribute. This is because by default targets are only visible to other targets in the same BUILD file. Bazel uses target visibility to prevent issues such as libraries containing implementation details leaking into public APIs. To build the sub package run

`bazel build //java/src/main/java/com/example/cmdline:runner`

To build a deployable version of the runner containing the dependencies class (Greeting.java), run:

`bazel build //java/src/main/java/com/example/cmdline:runner_deploy.jar`

This creates runner_deploy.jar, which you can run standalone away from your development environment since it contains the required runtime dependencies. Run the file with

`bazel-bin/java/src/main/java/com/example/cmdline/runner`


## Python

We have created two Python repositories / sub-folder to demonstrate cross dependency across projects. We have one main package and one library package.

### Build

To build the main python project run

`bazel build python_main:greetings`

To build the python common library project run

`bazel build python_util:greeting_class`

### RUN

`bazel run python_mail:greetings`

You cannot run the python common library since this is defined as a library package in the Bazel BUILD file, and is supposed to be run by other Python packages.

### Test

you can run the test implemented for the Python common library by running

`bazel test python_util:test_greeting_class`