# Professional Resume using LaTeX and Overleaf

A complete beginner-friendly tutorial for creating a professional, ATS-friendly resume using **LaTeX** and **Overleaf**.

This tutorial is designed for:

- Undergraduate students
- Postgraduate students
- PhD scholars
- Software Engineers
- Data Scientists
- Academic researchers

---

# Files in this Folder

```
Overleaf/
├── README.md
├── resume.tex
└── images/
```

| File | Description |
|------|-------------|
| `resume.tex` | Main LaTeX resume template |
| `README.md` | Step-by-step tutorial |
| `images/` | Screenshots used in this tutorial |

---

# What You Will Learn

By the end of this tutorial, you will be able to:

- Install nothing (Overleaf runs in your browser)
- Understand the structure of a LaTeX document
- Edit your resume
- Add experience, education, projects, and skills
- Generate a professional PDF
- Keep your resume under version control using GitHub

---

# Prerequisites

You only need:

- A web browser
- A free Overleaf account
- Basic computer knowledge

---

# Step 1 – Create an Overleaf Account

Go to

https://www.overleaf.com

Create a free account.

---

# Step 2 – Create a Blank Project

Click

```
New Project
```

↓

```
Blank Project
```

↓

Give it a name like

```
My Resume
```

![e918b367d3a700b2de14ef67bb81d766.png](../../_resources/e918b367d3a700b2de14ef67bb81d766.png)
---

# Step 3 – Upload the Resume Template

Delete the default files.

Upload

```
resume.tex
```

![bf959cf1bda25b045fd697af66336a95.png](../../_resources/bf959cf1bda25b045fd697af66336a95.png)

# Step 4 — Compile

Click

```
Recompile
```

Overleaf automatically builds your PDF.

Suggested screenshot

```
images/compile.png
```

---

# Understanding the LaTeX File

Every LaTeX document has two major parts

```
Preamble
```

and

```
Document
```

Example

```latex
\documentclass{article}

...

\begin{document}

Content goes here

\end{document}
```

---

# The Preamble

Everything before

```latex
\begin{document}
```

controls the appearance.

Example

```latex
\documentclass[10.5pt,a4paper]{article}
```

This selects

- Article class
- Font size
- Paper size

---

# Packages

Packages add new features.

Example

```latex
\usepackage{hyperref}
```

adds hyperlinks.

```latex
\usepackage{geometry}
```

controls margins.

```latex
\usepackage{enumitem}
```

controls lists.

```latex
\usepackage{microtype}
```

improves typography.

---

# Margins

```latex
\usepackage[left=0.65in,right=0.65in,top=0.55in,bottom=0.55in]{geometry}
```

Change these values to make your resume

- more compact
- more spacious

---

# Creating Sections

This template defines

```latex
\sectionline
```

Example

```latex
\sectionline{Experience}
```

Produces

```
EXPERIENCE
-----------------------------
```

---

# Name

Edit

```latex
{\Large \textbf{Vibhu Gautam}}
```

Replace with

```latex
{\Large \textbf{Your Name}}
```

---

# Contact Details

Replace

```latex
Paonta Sahib
```

with your location.

Replace

```latex
Phone Number
```

Replace

```latex
Email
```

Replace

```latex
LinkedIn
```

---

# Profile

Keep this section short.

Good profile

```
Machine Learning Engineer with experience in Computer Vision,
Deep Learning and Cloud AI.
```

Avoid

- long paragraphs
- personal objectives
- unnecessary adjectives

---

# Skills

Current

```latex
\textbf{Platforms}
```

You can change to

```
Programming

Cloud

Frameworks

Libraries

Tools

Databases
```

---

# Experience

Each experience follows

```latex
\textbf{Job Title}
```

↓

```latex
Company
```

↓

Bullet points

Example

```latex
\textbf{Software Engineer}

Google

\begin{itemize}

\item ...

\item ...

\end{itemize}
```

---

# Writing Good Bullet Points

Instead of

```
Worked on Python
```

Write

```
Developed REST APIs using FastAPI reducing deployment time by 40%.
```

Use action verbs

- Built
- Designed
- Developed
- Improved
- Automated
- Reduced
- Increased
- Optimized

---

# Education

Example

```latex
M.Sc. Computer Science
```

↓

University

↓

Year

---

# Publications

Example

```
IEEE
Springer
Elsevier
NeurIPS
ICML
CVPR
```

---

# Certifications

Example

```
AWS

Azure

Google Cloud

TensorFlow

NVIDIA
```

---

# Hyperlinks

Example

```latex
\href{https://linkedin.com}{LinkedIn}
```

---

# Bold Text

```latex
\textbf{Python}
```

---

# Italics

```latex
\textit{University of Southampton}
```

---

# Line Breaks

```latex
\\
```

moves to next line.

---

# Bullet Lists

Example

```latex
\begin{itemize}

\item First

\item Second

\end{itemize}
```

---

# Common Errors

## Missing bracket

Wrong

```latex
\textbf{Name
```

Correct

```latex
\textbf{Name}
```

---

## Missing end document

Always end with

```latex
\end{document}
```

---

# Export PDF

Click

```
Download PDF
```

Suggested screenshot

```
images/pdf-download.png
```

---

# ATS Tips

✔ One page

✔ Professional email

✔ LinkedIn

✔ GitHub

✔ Quantify achievements

✔ Strong action verbs

✔ Avoid tables

✔ Avoid text boxes

✔ Avoid images

✔ Save as PDF

---

# Recommended Sections

- Profile
- Skills
- Experience
- Projects
- Education
- Publications
- Certifications
- Awards
- Languages

---

# Resources

LaTeX Documentation

https://www.latex-project.org

Overleaf

https://www.overleaf.com

Detexify (Find Symbols)

https://detexify.kirelabs.org

CTAN Packages

https://ctan.org

---

# License

MIT License

---

# Author

**Vibhu Gautam**

Professor of Practice

School of Computer Science

UPES Dehradun

GitHub

https://github.com/vibhug0077