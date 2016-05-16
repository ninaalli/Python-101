Root /
folder ~

.cd - current directory
.pwd - previous working directory (shows absolute path, from root directory to where you are now)
.mkdir - make directory
.ls - list

. (dot) stands for current directory
..(dot dot) will list structure of the parent directory
to make a file: touch 

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   reset      Reset current HEAD to the specified state
   rm         Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect     Use binary search to find the commit that introduced a bug
   grep       Print lines matching a pattern
   log        Show commit logs
   show       Show various types of objects
   status     Show the working tree status

grow, mark and tweak your common history
   branch     List, create, or delete branches
   checkout   Switch branches or restore working tree files
   commit     Record changes to the repository
   diff       Show changes between commits, commit and working tree, etc
   merge      Join two or more development histories together
   rebase     Forward-port local commits to the updated upstream head
   tag        Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch      Download objects and refs from another repository
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.


To clone a repository: 
highlight the https from the page, 
 type git clone and the address to pull down the repository
 
 Master 
   Everyone takes from the master file for their own branches
   Make your own branch everyday, to push code up and not overwrite Master
   Local copy is your machine, remote is the master
   
   In Bash:
        Ninas-Air:MonsterAcademy ninaalli$ cd week1-day1/
        Ninas-Air:week1-day1 ninaalli$ git branch
        * master
        Ninas-Air:week1-day1 ninaalli$ git checkout -b ninaalli
        Switched to a new branch 'ninaalli'
        Ninas-Air:week1-day1 ninaalli$ git branch
        master
      * ninaalli
      Ninas-Air:week1-day1 ninaalli$ 

git branch -b (will auto switch to the new repository)
git branch NAME will show only the branch, not switch

iif you type ATOM in Bash, it opens a blank atom page
if you type atom in the folder, Atom . (this will open the current directory into the text editor)

git commit to make sure you see what was changed, you have to tell it to change and commit it 
not tracked (files that did not exist prior, if tracked and modified will be red. 

to stage a commit, git add (place path here)

to create a new file in the file you are in: touch (new name for file)
When you commit, you commit all of them - if you dont want them there:
      git reset (file name)

anything that follows git is a git command
-m is short for message (sees it as a string - a variation of characters)
git commit -m "comment what you did" (for every 20-30 changes committed, this is important)
git diff (shows you the changes in the codes

after git add, always do git status to make sure you arent surprised by the outcomes.

git push goes to the remote git
git push origin ninaalli
   shows what is in the file
   git remote
   git remote -v
   
Ninas-Air:week1-day1 ninaalli$ git remote -v
origin	https://github.com/gila-monsters-2016/week1-day1.git (fetch)
origin	https://github.com/gila-monsters-2016/week1-day1.git (push)
Ninas-Air:week1-day1 ninaalli$ 
***to FETCH: it will go to the remote we specify and will take the directory and bring it down to our github, it wont combine the two.
   PULL- fetches changes from remote and combines them into the local repository
      if you are on your branch, do not PULL
      if you checkout to Master, it will merge all the branches, 
         to get any changes you will have to merge it.
         
      ALWAYS BE AWARE OF THE BRANCH YOU ARE ON.
      GitHub will try to find the differences prior to a commit so you can work on changes so there is no conflict (which you have to go in and resolve)
      
DAY 1 most important lessons:
   Git
      branch (have to be on the branch to do all of this)
      checkout -b <branch name>
      status
      add <path to the file>
      commit -m <message>
      push <name of the remote><name of the branch>
      
      git stash apply - will make it look like 
