# Lab 11 – GitHub Actions Workflow

**Student:** Matthew Sabadac  
**Course:** SWE 325/525  
**Programming Language:** Python

## Project Description

For this lab, I created my own GitHub repository and set up a GitHub Actions workflow to run a Python program. The workflow runs automatically whenever I push changes to the main branch. I also set it up so I can run it manually from the Actions tab.

My Python program uses an environment variable called `WHO_TO_GREET` to get a name. If the variable isn't available, the program uses "World" instead. It then prints a greeting along with a message saying that the program is running inside GitHub Actions.

## Repository Files

- `hello.py` – The Python program that prints the messages.
- `.github/workflows/hello.yml` – The workflow file that tells GitHub Actions what to do.
- `README.md` – Information about my project and how everything works.

## Expected Program Output

```text
Hello GitHub Actions students!
This program is running inside GitHub Actions.
```

## How the Workflow Works

**1. What is the purpose of the `on` section?**

The `on` section tells GitHub when the workflow should run. For my project, it starts automatically when I push changes to the main branch, but I can also start it manually.

**2. What does `workflow_dispatch` do?**

It lets me run the workflow myself by clicking the Run workflow button in GitHub Actions. This way, I don't have to make changes to my code just to run it again.

**3. What does `runs-on` specify?**

It tells GitHub what kind of computer should run the job. I used `ubuntu-latest`, which means my workflow runs on a Linux computer provided by GitHub.

**4. Why is `actions/checkout` needed?**

This step gets the files from my GitHub repository and makes them available to the runner. Without it, the workflow wouldn't have my Python file to run.

**5. What does the language setup action do?**

The `actions/setup-python` step makes sure the runner has the Python version I selected. This allows my program to run in the correct environment.

**6. What is the difference between compiling and running a program?**

Compiling is when source code gets translated into a form the computer can execute. Running is when the computer actually executes the program. Since my project uses Python, I don't need to compile it separately before running it.

**7. Where can I see the program output?**

I can find the output in the Actions tab on GitHub. I just open the workflow run, select the job, and expand the Run Python program step to see the messages.

**8. What is the difference between a workflow, a job, and a step?**

A workflow is the whole automated process that GitHub follows. A job is a group of tasks that runs on a runner, and a step is one specific task inside that job. For example, my workflow has a job that sets up Python and runs my program.

## Testing Results

**Automatic Execution**

After adding my Python program to the main branch, GitHub Actions automatically started the workflow. I checked the Actions tab and confirmed that it finished successfully. The program also displayed both expected messages.

**Manual Execution**

I also tested the workflow manually by going to the Actions tab, selecting my workflow, and clicking Run workflow. I kept the main branch selected and started the run. It completed successfully, and I checked the logs to make sure the program printed the correct output.

## AI Usage Statement

I used AI assistance to help me understand the assignment instructions, write the Python program and workflow file, and explain some of the GitHub Actions concepts. I completed the steps in my GitHub repository and tested both the automatic and manual workflow runs to make sure everything worked correctly.
