"""
                 ---------------------------------------                                   
                 |Git and GitHub Tutorial For Beginners|
                ----------------------------------------
                
YouTube Tutorial Link: https://www.youtube.com/watch?v=3fUbBnN_H2c

Git:
  Git is a version control system that allows one or more people to work on
  the same code base, on the same project.
For e.g.:You and I could be working on same project, I can see your changes,
you can see my changes,we can work on same file, if we have some conflicts,
we can resolve the conflicts and basically we have the history of entire
project as we build an application.  

GitHub:(Bought by Microsoft)
    GitHub is the hosting platform that allows us to host our project somewhere
on the cloud.So, most popular hosting provider for git projects is github,
gitbucket,git lab ,code commit and many others.

How Git Works?  --Img 1
    Working Directory: Local Computer
    Staging area:
Commands:
    Git add
    Git Commit: Commit is a simply save point.--Img 2
        You made an app, you commited one file, if suppose you make some
        changes in another file , you commit another file, likewise and so
        on,many file commited.
    Git Push:Local Machine --Img 3
        The problem is that if suppose our computer dies,let's take an example
        computer is not starting, so now you've lost all of those changes ,
        well what we need actually is to take our changes and then store it
        in remote server, where actually host our project.
        The most git providers are github by microsoft,bitbucket and aws code
        commit, most popular GitHub.
        So, how do we take the changes from local machine to the remote server,
        so way we do it is by simply issuing the git push command.
        So, now when we take the changes from our local machine, we push
        it to a remote server if our computer crashes or we have any issues
        with our computer then the changes are in the remote server and what's
        really great about this is that now you can work and collaborate with
        people all around word. ---Img 4

Installing Git:
     Guidelines: https://github.com/git-guides/install-git
     Windows: https://gitforwindows.org/

Learn the Git Right Way:
    Windows: GitBash

Verify Installation:
    git --version
        git version 2.30.1.windows.1
    git init---------(.git folder created)
        Initialized empty Git repository in F:/Bhaskar_Python/Git and
        GitHub Tutorial/.git/
    git --help
        For help to learn about git commands.
    ctrl + l
        To clear the screen.

Git Setup:
    Configure Profile:
        git config --global user.name "bhaskarwagatakar"
        git config --global user.email "bhaskarwagatakar@gmail.com"
        git config --global color.ui auto

        git config
        ctrl + l
        git config -l
            Configuration in your system.

Git Init:
    Repositories in git contain a collection of files of various different
    versions of a project.
    git init .---------(.git folder created)---- current directory
        Reinitialized existing Git repository in F:/Bhaskar_Python/Git and
        GitHub Tutorial/.git/

Git Add:
    git status  -----------changes made
    
    git add movies_released_IMDB.ipynb -------------- imp

    git rm --cached movies_released_IMDB.ipynb ---not imp

    git status ------back to normal

    git add . (dot means add all files downwords)-----------imp

    git rm -r --cached .  --------not imp

    git status

    git status -A    ----------(if you want to add every single file in each
                                folder)

    git status

    git add .  (we generally use)

Commits:
    git commit -m "movies file added" (Here m means meassage and it must
                                        be descriptive.)

    git log

    git -diff - Show changes between commits, commit and working tree, etc.--not
                imp now
        Show changes between the working tree and the index or a tree, changes
        between the index and a tree, changes between two trees, changes
        resulting from a merge, changes between two blob objects, or changes
        between two files on disk. (https://git-scm.com/docs/git-diff)

Ammend Commits: ------not imp now
    git ammend -m ---(simply to change message of the added file)
    git ammend -m "I want to change message"
    On the command line, navigate to the repository that contains the commit
you want to amend. Type git commit --amend and press Enter. In your text editor,
edit the commit message, and save the commit. You can add a co-author by adding
a trailer to the commit.

Git Push:
     Git Push  ---Img 5
       Computr break, virus or if computer corrupted or we loose acces to
       computer then we loose the project. It takes copy from local machine and store
       it to a local server.

GitHub: --Img 6
    A platform for hosting and collaborating on Git repositories.(GitHub repo)
    https://github.com/
        Go sign up and create an account.

Create Repo:
    New Repository:
        Learning_git
            Public : free
            Private: Paid
-----------------------------------------------------------
---Img 8

…or create a new repository on the command line
echo "# Git_and_Github_Learning" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:bhaskarwagatakar/Git_and_Github_Learning.git
git push -u origin main
---------------------------------------------------------
…or push an existing repository from the command line      (use this)
git remote add origin git@github.com:bhaskarwagatakar/Git_and_Github_Learning.git
git branch -M main
git push -u origin main
-----------------------------------------------------------
SSH Keys Set Up:

    1)Go to settings.
    2)Click on left side SSH and GPG keys.
    3)Click on generating SSH keys.
    4)Click on Generating a new SSH key and adding it to the ssh-agent→.
        Generating a new SSH key
            Open Git Bash.
                ssh-keygen -t ed25519 -C "your_email@example.com"

        Adding your SSH key to the ssh-agent
            eval `ssh-agent -s`

            ssh-add ~/.ssh/id_ed25519

        Adding a new SSH key to your GitHub account
           clip < ~/.ssh/id_ed25519.pub

Git Push:
    git push -u origin main

Git Pull:  ---Img 9
    git pull
    The git pull command is used to fetch and download content from a remote
    repository and immediately update the local repository to match that content.
    Merging remote upstream changes into your local repository is a common task
    in Git-based collaboration work flows.

Branches:  ---Img 10
    A branch represents an independent line of developement.
        git branch   ----to know current branch ---not execute
        git checkout -b main ---to switch branch   ------------we use this command.

Working with branches:
        git branch  ----to know current branch
        git branch -r  ----to know current remote branch
        git branch -a  ----to check all branches
        git branch branchname (git branch feature-a) ----to create to new branch
        git branch -a --to check again
        git checkout feature-a ---to switch out to particular branch
        git checkout -   --to checkout previous branch
        git branch -d branchname ----to delete branch ---we don't use this command.

Git clone   ----to copy repository from github----imp

Building your Portfolio  ----on GitHub Profile

Exploring GitHub   ------ Learning new things about programming.

Learn about Opensource contribution projects, Freelancing

Git Desktop   ----------- Desktop app version.


Main=Master
Pull Requests
Merging PR's: Merging pull requests
Git Workflow
Dealing with conflicts
Merging Conflicts
Rebase
Git Rebase
Git Rebase Recap
Git Clients
Git POD
Building your Portfolio
Exploring GitHub
Open Source Software


        

    

            





    
    
        
    

        




"""
