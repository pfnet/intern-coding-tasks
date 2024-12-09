# JE04 [10-Days] Employment Experience in the Development and Operation of a web system for Matlantis, a general-purpose atomic-level simulator

## Coding Task

Please proceed to the following URL to access the coding task: (omit URL)

Although the exam consists of six problems, you **are not required to solve all of them**.
For this specific theme, you are expected to solve three problems listed below:

- 1 (Undisclosed problem)
- 2 (Undisclosed problem)
- 3 Winning Probability of Poker

Please provide the solutions using one of the following programming languages:

- Python3
- Go
- TypeScript

## Thematic Task

### Question

We provide a SaaS (Software-as-a-Service) for a chat-based paper summarization service using an LLM (Large Language Model). As a new feature, we have decided to develop a functionality that allows users to perform additional training of the LLM used for summarization using their own data. This feature is referred to as the "additional training feature."

### Assumptions and Requirements

This service operates on cloud platforms such as AWS or GCP. The requirements for the additional training feature are outlined as follows.

#### Frontend

The frontend will consist of two screens:

1. Execution Screen: This screen is used to initiate the additional training process. It contains a form with fields for entering a name and uploading the training dataset.
2. List Screen: This screen displays the names, training start and end times, and the number of ongoing and completed additional training processes.

The system should not allow duplicate names for processes by the same user. The display of epoch numbers on the list screen does not need to be in real-time, but the latest value should be updated approximately every 5 minutes.

#### Backend

The backend needs to incorporate the functionality to execute the additional training process, which must meet the following requirements:

- The execution of the additional training process requires at least one GPU. It is expected to take a minimum of one hour for the process to complete.
- Users should be able to upload training datasets up to a maximum size of 10GB.
- The server should be capable of running at least two or more additional training processes in parallel.
- Any additional training process running for more than three days should be considered abnormal and terminated.
- There is no need to develop a new authentication and authorization mechanism for the backend, as an existing one is already in place.
- The frequency of requests to the backend is expected to vary due to time and social media spreading.

### Your Task

If you were to participate in the development of this new feature, please summarize the points that you consider important in the field or fields of your expertise in a report. You do not need to cover all fields. Please focus on the fields you are most comfortable with.

- **If specific libraries or services required for implementation are explicitly mentioned, bonus points will be awarded.**
  - You may mention cloud services such as AWS or GCP.
- As an example, the following points are expected:
  - Frontend, UX, API Design
    - How will you design the upload process for large training datasets?
    - Is there anything you can do to improve UX during the upload?
    - How will you validate the dataset names provided by the user?
  - Backend
    - How will you implement the additional training process?
    - What kind of implementation can be considered for users to check the progress of the training?
    - What managed services would be efficient to use in order to reduce development effort and operational costs? What are the disadvantages of introducing managed services?
    - How will you implement testing?
    - Are there any specific security aspects to consider?
  - Infrastructure
    - It would be too costly to keep multiple high-priced GPUs running at all times. How will you implement auto-scaling?
    - What can be done to save infrastructure costs other than GPUs?
  - Requirements
    - Are there any additional requirements that can be added to improve the user experience?
    - Are there any additional requirements that can be added to enhance security?

You can also include additional points if you like, and it is not necessary to cover all points. **Please share what you believe is important from a technical perspective and where you think you can make a significant contribution in implementing the additional processing feature.**

In your answers, do not include any improvements or innovations that can bring a sense of novelty.

### Submission instructions

Submit your answers in a PDF file named `survey.pdf` that does not exceed two A4-sized pages.
