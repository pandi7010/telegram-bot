from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Command Handlers
async def start(update, context):
    await update.message.reply_text("Hello! Welcome to Pandiselvam's professional bot. Use /help to see available commands.")

async def help(update, context):
    await update.message.reply_text("""
    The following commands are available:
    
    /start -> Welcome to the bot
    /skills -> View Pandiselvam's technical skills
    /projects -> Explore Pandiselvam's projects
    /education -> Learn about Pandiselvam's educational background
    /achievements -> See Pandiselvam's achievements and certifications
    /internship -> Get details of Pandiselvam's internship experience
    /contact -> Contact information
    /interest -> Explore Pandiselvam's area of interests
     """)

async def skills(update, context):
    await update.message.reply_text("""
    Technical Skills:
    - Programming Languages: Python, Java, SQL
    - Web Development: HTML, CSS, JavaScript, Bootstrap, Flask
    - Tools and Platforms: Git, GitHub, Bitbucket, Jira, Figma, AWS, Power BI
    - Additional Skills: Prompt Engineering
    """)

async def projects(update, context):
    await update.message.reply_text("""
    Projects:
    - Intelligent Meteorological Data Station: Real-time weather monitoring using DHT11, BMP180 sensors, Raspberry Pi, and ESP8266.
    - Home Automation System: Remote control of home appliances using Raspberry Pi Pico W and Blynk App.
    - Food Order Platform: Responsive website using HTML, CSS, Bootstrap. [Food Munch](https://pandi7010.github.io/food-munch/)
    - Generative AI Application: AI chatbot using HTML, CSS, JavaScript, Python. [AI Chatbot](https://pandiaichatbot.ccbp.tech/)
    - Project Idea Suggestion App: Idea brainstorming platform. [Idea Hub](https://pandiideahub.ccbp.tech/)
    """)

async def education(update, context):
    await update.message.reply_text("""
    Education:
    - B.E Electronics and Communication Engineering (2022-2026)
      V.S.B Engineering College, Karur, India (CGPA: 7.7)
    - Higher Secondary Education:
      S.P.M OXFORD Matric Hr Sec School, Dindigul (Class 12: 73.5%, Class 10: 70.0%)
    """)

async def achievements(update, context):
    await update.message.reply_text("""
    Achievements:
    - Patent: EXPERT INTELLIGENCE: AI-POWERED REAL-TIME KNOWLEDGE ACCESS
      (Application No: 202441079560, Published Date: 25/10/2024)
    - Hackathons: Smart India Hackathon (2024), Accenture Innovation Challenge (2023)
    - Certifications:
      - Java Foundations – Infosys Springboard
      - IoT – LinkedIn Learning
      - Prompt Engineering and Generative AI – LinkedIn Learning
    """)

async def internship(update, context):
    await update.message.reply_text("""
    Internship Experience:
    - Software Development Intern at Pearlax Corporation LLP, Bengaluru (June 2024 – July 2024)
    - Worked on Python and Flask-based applications, gaining proficiency in front-end development.
    """)

async def contact(update, context):
    await update.message.reply_text("""
    Contact Information:
    - Email: pandiselvam1216@gmail.com
    - Phone: +91 8111093310, +91 7010953595
    - GitHub: [GitHub Profile](https://github.com/pandi7010)
    - LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/pandiselvam-r/)
    """)

async def interest(update, context):
    await update.message.reply_text("""
    Areas of Interest:
    - Skating
    - Product development
    """)

# Initialize Application
Token = "7580464107:AAGtnHUqUbXMzlG3u45EWMP6Y21xuHkgJ3k"
app = Application.builder().token(Token).build()

# Command Handlers
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', help))
app.add_handler(CommandHandler('skills', skills))
app.add_handler(CommandHandler('projects', projects))
app.add_handler(CommandHandler('education', education))
app.add_handler(CommandHandler('achievements', achievements))
app.add_handler(CommandHandler('internship', internship))
app.add_handler(CommandHandler('contact', contact))
app.add_handler(CommandHandler('interest', interest))

# Start the bot
app.run_polling()
