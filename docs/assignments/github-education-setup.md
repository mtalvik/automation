# GitHub Education Setup

## Overview

This guide helps you set up GitHub Education features for your automation course, including GitHub Classroom, student benefits, and educational resources.

## GitHub Education Benefits

### For Educators
- **GitHub Classroom** - Automated assignment distribution and grading
- **Private repositories** - Unlimited private repos for educational use
- **GitHub Actions** - 2,utes/month for CI/CD
- **GitHub Packages** - 500MB storage for container images
- **Priority support** - Educational support team

### For Students
- **Student Developer Pack** - Access to premium developer tools
- **Private repositories** - Unlimited private repos
- **GitHub Actions** - 2,utes/month
- **GitHub Packages** - 500MB storage
- **Learning resources** - GitHub Learning Lab courses

## Setup Process

#### Apply for GitHub Education

#### Educator Application
1. Go to [GitHub Education](https://education.github.com)
2. Click "Get benefits for teachers"
3. Fill out the application:
   - **Institution:** Your school/university
   - **Course details:** Automation course information
   - **Student count:** Expected number of students
   - **Use case:** Describe how you'll use GitHub

#### Required Information
- Official email address from your institution
- Course syllabus or description
- Expected number of students
- Duration of the course

#### GitHub Classroom Setup

#### Create Classroom
1. Go to [GitHub Classroom](https://classroom.github.com)
2. Click "New classroom"
3. Fill in details:
   - **Classroom name:** "Infrastruktuuri Automatiseerimine"
   - **Organization:** Create or use existing
   - **Visibility:** Private (recommended)

#### Organization Setup
```yaml
Organization name: mtalvik-automation-class
Description: Automation course for ITS-24 students
Visibility: Private
Members: Students and teaching assistants
```

#### Assignment Creation

#### Assignment Template Structure
```yaml
Assignment:
  name: "Week X: Topic Name"
  repository: "automation-week-X-starter"
  template: true
  private: true
  autograding: true
  deadline: "2024-XX-XX"
```

#### Autograding Configuration
Use the `.github/classroom/autograding.json` file in your repository:

```json
{
  "tests": [
    {
      "name": "Infrastructure Test",
      "setup": "apt-get update && apt-get install -y ansible",
      "run": "ansible-playbook playbook.yml --check",
      "points": 50
    }
  ]
}
```

#### Student Onboarding

#### Student Registration Process
1. **Share classroom link** with students
2. **Students accept invitation** to join classroom
3. **Students link GitHub account** to classroom
4. **Students start assignments** from classroom interface

#### Student Setup Instructions
```markdown
# Student Setup Guide

### GitHub Account
- Create GitHub account if you don't have one
- Use your school email address
- Complete your profile

### Join Classroom
- Click the classroom invitation link
- Accept the invitation
- Link your GitHub account

### Student Developer Pack
- Apply for Student Developer Pack
- Access premium tools and services
- Use for course projects

### First Assignment
- Click "Start assignment" in classroom
- Clone your repository
- Follow assignment instructions
```

#### Assignment Management

#### Creating Assignments
1. **Go to classroom dashboard**
2. **Click "New assignment"**
3. **Fill in assignment details:**
   - Title and description
   - Repository template
   - Deadline and points
   - Autograding tests

#### Assignment Types
- **Individual assignments** - Each student gets private repo
- **Group assignments** - Teams share repository
- **Template repositories** - Pre-populated with starter code

#### Grading and Feedback

#### Automated Grading
- **GitHub Actions** run tests automatically
- **Results displayed** in classroom interface
- **Feedback provided** through pull requests

#### Manual Grading
- **Review student code** in their repositories
- **Provide feedback** through issues or comments
- **Grade assignments** in classroom interface

#### Student Benefits

#### Student Developer Pack
Students get access to:
- **AWS Educate** - $75 in credits
- **DigitalOcean** - $50 in credits
- **Namecheap** - Free domain name
- **JetBrains** - Free professional IDEs
- **GitHub Desktop** - Git GUI client

#### Learning Resources
- **GitHub Learning Lab** - Interactive courses
- **GitHub Skills** - Step-by-step tutorials
- **Documentation** - Comprehensive guides

#### Best Practices

#### For Educators
- **Set clear deadlines** and communicate them
- **Provide detailed instructions** for each assignment
- **Use templates** to ensure consistency
- **Enable autograding** for immediate feedback
- **Monitor student progress** regularly

#### For Students
- **Read instructions carefully** before starting
- **Ask questions** in GitHub Discussions
- **Submit work on time** to avoid penalties
- **Use version control** effectively
- **Document your work** thoroughly

#### Troubleshooting

#### Common Issues
1. **Students can't access classroom**
   - Check invitation links
   - Verify GitHub account status
   - Ensure proper organization membership

2. **Assignments not appearing**
   - Check repository permissions
   - Verify template repository setup
   - Ensure proper classroom configuration

3. **Autograding not working**
   - Check GitHub Actions permissions
   - Verify test configuration
   - Review workflow logs

#### Support Resources
- [GitHub Education Support](https://support.github.com/contact/education)
- [GitHub Classroom Help](https://classroom.github.com/help)
- [GitHub Community Forum](https://github.community/)

#### Integration with Course Materials

#### Linking to Course Website
- **Include classroom links** in course materials
- **Embed assignment instructions** in course website
- **Provide direct access** to student repositories

#### Course Website Integration
```markdown
## Week X Assignment
- [Start Assignment](https://classroom.github.com/a/YOUR_ASSIGNMENT_ID)
- [Assignment Instructions](docs/assignments/week-X.md)
- [Student Resources](docs/student-resources.md)
```

## Monitoring and Analytics

### Classroom Analytics
- **Assignment completion rates**
- **Student engagement metrics**
- **Code quality statistics**
- **Collaboration patterns**

### Student Progress Tracking
- **Individual repository activity**
- **Assignment submission history**
- **Code contribution patterns**
- **Learning progression**

## Advanced Features

### Custom Autograding
- **Write custom tests** for specific requirements
- **Integrate with external tools** (Docker, Ansible)
- **Provide detailed feedback** on failures
- **Support multiple test types**

### Integration with LMS
- **Grade passback** to institutional systems
- **Roster synchronization** with student information systems
- **Assignment distribution** through existing platforms
- **Progress reporting** to administrators
