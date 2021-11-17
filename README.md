# Mono repository

A monorepo is a unified code base for multiple projects sharing dependencies, libraries etc. Monorepos are often great for microservices because they stay integrated and share infrastructure in the code base. A multirepo is a decentralized and bottom-up way of keeping your code while monorepos organizes as centralized and top-down. 

## Monorepo strengths over multirepo
Multirepos often require a lot publishing and versioning handling of the repositories / services. If you commit changes in a repo in a multirepo ecosystem, other repositories dependant on that repo will also potentially be affected by that change. Therefore, you have to verify that the other dependant repositories still works with the changes you introduced to the code base. However, you could also keep the dependant repositories pinned to the old version of the repo you commited changes to, avoiding the integration verification. This will kick the integration problem down the road but will have to be solved at a later time. Then the integration problem will have to be solved by someone else without context or by you when you have forgotten all about it. You have no publishing / versioning in a monorepo, the consumers are all in the same repo. Thus, integration crashes are imminent and must be adressed immediately. Monorepos are also easier to refactor, debug, reuse code and avoid code duplication and keep a unified change history.

# Bazel build and test tool
Bazel is an open-source build and test tool similar to Maven. It uses a human-readable, high-level build language. Bazel supports projects in multiple languages and builds outputs for multiple platforms. Bazel supports large codebases across multiple repositories, and large numbers of users. The ultimate goal of Bazel is to speed things up when we work with a monorepo which grows in code base size and number of contributors.  Bazel is used by and continuously developed and improved by Google and has a large community base. It is a very useful tool when you have many files and dependencies.

[See Bazel documentation](https://docs.bazel.build/versions/main/bazel-overview.html)

## Bazel benefits

* __High-level build language.__ Bazel uses an abstract, human-readable language to describe the build properties of your project at a high semantical level. Unlike other tools, Bazel operates on the concepts of libraries, binaries, scripts, and data sets, shielding you from the complexity of writing individual calls to tools such as compilers and linkers.

* __Bazel is fast and reliable.__ Bazel caches all previously done work and tracks changes to both file content and build commands. This way, Bazel knows when something needs to be rebuilt, and rebuilds only that. To further speed up your builds, you can set up your project to build in a highly parallel and incremental fashion.

* __Bazel is multi-platform.__ Bazel runs on Linux, macOS, and Windows. Bazel can build binaries and deployable packages for multiple platforms, including desktop, server, and mobile, from the same project.

* __Bazel scales.__ Bazel maintains agility while handling builds with 100k+ source files. It works with multiple repositories and user bases in the tens of thousands.

* __Bazel is extensible.__ Many languages are supported, and you can extend Bazel to support any other language or framework.


# Build project commands

## Build
`bazel build //java:ProjectRunner`

`bazel build //java/src/main/java/com/example/cmdline:runner`

To build a deployable version of the runner containing the dependencies class (Greeting.java), run:

`bazel build //java/src/main/java/com/example/cmdline:runner_deploy.jar`

This creates runner_deploy.jar, which you can run standalone away from your development environment since it contains the required runtime dependencies.

## Run
`bazel-bin/java/ProjectRunner`

`bazel-bin/java/src/main/java/com/example/cmdline/runner`

## Dependency graph

The dependency graph of the ProjectRunner java class can be first generated with

`bazel query  --notool_deps --noimplicit_deps "deps(//java:ProjectRunner)" --output graph`

Then visualized by copying the string output to http://www.webgraphviz.com/