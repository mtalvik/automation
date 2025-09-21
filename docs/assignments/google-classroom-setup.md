# Google Classroom Integration

## Overview

This guide helps you integrate your automation course with Google Classroom for seamless assignment management and student tracking.

## Setup Steps

#### Google Classroom Configuration

#### Create Your Class
1. Go to [Google Classroom](https://classroom.google.com)
2. Click "Create class"
3. Fill in class details:
   - **Class name:** "Infrastruktuuri Automatiseerimine - ITS-24"
   - **Section:** "Täiskasvanute klass"
   - **Subject:** "Computer Science"
   - **Room:** "Online"

#### Class Settings
- **Class code:** Share with students for easy joining
- **Stream settings:** Allow students to post and comment
- **Classwork settings:** Enable assignment creation

#### Assignment Templates

#### Weekly Assignment Structure
Each week follows this pattern:

**Title:** `Nädal [X]: [Topic] - [Assignment Type]`
**Instructions:** Copy from your course materials
**Points:** 100
**Due date:** Set according to your schedule
**Topic:** Create topics for each module

#### Assignment Types
1. **Lab Assignment** - Practical hands-on work
2. **Homework** - Theoretical and practical combination
3. **Reading Assignment** - Documentation and research
4. **Project** - Larger integrated assignments

#### Integration with GitHub

#### Linking GitHub Repositories
1. In each assignment, include:
   - Link to GitHub Classroom assignment
   - Instructions for repository setup
   - Submission requirements

#### Example Assignment Instructions
```markdown
## Ülesanne: Docker Fundamentals Lab

### Ülesanne 1.1: GitHub Repository
1. Kliki [Start Assignment](https://classroom.github.com/a/YOUR_ASSIGNMENT_ID)
2. Klooni oma repository: `git clone [YOUR_REPO_URL]`
3. Järgi juhiseid `README.md` failis

### Ülesanne 2.1: Lab Töö
1. Loo Dockerfile
2. Käivita container
3. Testi rakendust

### Ülesanne 3.1: Esitamine
1. Push kõik muudatused GitHub'i
2. Lisa link Google Classroom'i
3. Lisa screenshot töötavast rakendusest
```

#### Grading Integration

#### Rubric Setup
Create consistent rubrics for each assignment type:

**Lab Assignment Rubric (100 points):**
- Functionality (60 points)
  - Code works correctly (30)
  - Follows best practices (20)
  - Error handling (10)
- Documentation (20 points)
  - README completeness (10)
  - Code comments (10)
- Submission (20 points)
  - On time (10)
  - GitHub repository (10)

#### Automated Grading
- Use GitHub Actions for automated testing
- Link test results to Google Classroom
- Provide detailed feedback

#### Student Management

#### Class Roster
- Import students from your institution's system
- Create student groups for collaborative work
- Track individual progress

#### Communication
- Use Google Classroom announcements for course updates
- Enable private comments for individual help
- Use the stream for general discussions

#### Assignment Templates

#### Template 1: Lab Assignment
```markdown
# Nädal [X]: [Topic] Lab

## Eesmärk
[Learning objectives]

## Vajalikud tööriistad
- [Tool 1]
- [Tool 2]

## Sammud
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Esitamine
- [ ] GitHub repository link
- [ ] Screenshot töötavast rakendusest
- [ ] README.md dokumentatsioon

## Hindamine
- Funktsionaalsus: 60%
- Dokumentatsioon: 20%
- Esitamine: 20%
```

#### Template 2: Reading Assignment
```markdown
# Nädal [X]: [Topic] Lugemine

## Lugemismaterjal
- [Link 1]
- [Link 2]
- [Documentation]

## Küsimused
1. [Question 1]
2. [Question 2]
3. [Question 3]

## Esitamine
- Vasta küsimustele Google Classroom'is
- Lisa oma mõtted ja küsimused
- Viita lugemismaterjalile

## Hindamine
- Vastuste täielikkus: 50%
- Mõtlemine ja analüüs: 30%
- Viited materjalile: 20%
```

#### Progress Tracking

#### Gradebook Setup
- Create categories for different assignment types
- Set up weighted grading
- Enable grade export

#### Analytics
- Track assignment completion rates
- Monitor student engagement
- Identify struggling students early

#### Best Practices

#### Communication
- Post weekly announcements
- Respond to student questions within 
- Use private comments for individual feedback

#### Assignment Management
- Post assignments at least one week in advance
- Provide clear, detailed instructions
- Include examples and templates

#### Feedback
- Provide specific, actionable feedback
- Use rubrics consistently
- Celebrate student achievements

## Troubleshooting

### Common Issues
1. **Students can't access GitHub Classroom**
   - Verify they have GitHub accounts
   - Check classroom invitation links
   - Ensure they're in the correct organization

2. **Assignment submissions not appearing**
   - Check GitHub repository permissions
   - Verify assignment links are correct
   - Ensure students pushed to correct branch

3. **Grading integration issues**
   - Test GitHub Actions workflows
   - Verify webhook configurations
   - Check API permissions

### Support Resources
- [Google Classroom Help](https://support.google.com/edu/classroom)
- [GitHub Classroom Documentation](https://classroom.github.com/help)
- [Course-specific help in GitHub Discussions](https://github.com/mtalvik/automation/discussions)
