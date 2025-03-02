from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for flash messages and sessions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    # In a real app, you would fetch projects from a database
    return render_template('projects.html')

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    # In a real app, you would fetch project details from a database
    return render_template('project_detail.html', project_id=project_id)

@app.route('/how_it_works')
def how_it_works():
    return render_template('how_it_works.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process contact form submission
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # You would handle this data (e.g., send email, save to DB)
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process login form
        email = request.form.get('email')
        password = request.form.get('password')
        # Validate credentials (in a real app)
        # Set session
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Extract form data
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Basic validation
        error = None
        
        # Check if all required fields are filled
        if not all([first_name, last_name, email, password, confirm_password]):
            error = 'All fields are required.'
        # Check if passwords match
        elif password != confirm_password:
            error = 'Passwords do not match.'
        # Check password length for security
        elif len(password) < 8:
            error = 'Password must be at least 8 characters long.'
        # Check email format
        elif '@' not in email or '.' not in email:
            error = 'Please provide a valid email address.'
            
        # In a real application, you would also:
        # 1. Check if email already exists in the database
        # 2. Hash the password before storing it
        # 3. Insert the new user into your database
        
        if error:
            flash(error, 'danger')
            return render_template('signup.html', 
                                   first_name=first_name,
                                   last_name=last_name,
                                   email=email)
        else:
            # Here you would add the user to your database
            # For example:
            # new_user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password)
            # db.session.add(new_user)
            # db.session.commit()
            
            flash('Account created successfully! Please log in.', 'success')
            return redirect(url_for('login'))
            
    return render_template('signup.html')

@app.route('/testimonials')
def testimonials():
    # In a real app, you would fetch testimonials from a database
    testimonials_data = [
        {
            'id': 1,
            'content': 'EcoLend helped me align my investments with my values. I\'m earning returns while supporting renewable energy projects that make a real difference!',
            'author': 'Sarah Johnson',
            'role': 'Investor since 2022',
            'image': 'https://randomuser.me/api/portraits/women/32.jpg',
            'rating': 5,
            'date': 'March 15, 2023'
        },
        {
            'id': 2,
            'content': 'As a small business focused on sustainability, EcoLend provided funding when traditional banks wouldn\'t. Their platform made the entire process transparent and seamless.',
            'author': 'Michael Rodriguez',
            'role': 'Clean Energy Entrepreneur',
            'image': 'https://randomuser.me/api/portraits/men/54.jpg',
            'rating': 4.5,
            'date': 'January 8, 2023'
        },
        {
            'id': 3,
            'content': 'The platform is intuitive and transparent. I can clearly see where my money goes and the impact it creates. It\'s investing with purpose, not just profit.',
            'author': 'Jennifer Lee',
            'role': 'Impact Investor',
            'image': 'https://randomuser.me/api/portraits/women/68.jpg',
            'rating': 5,
            'date': 'April 22, 2023'
        },
        {
            'id': 4,
            'content': 'I\'ve tried several investment platforms, but EcoLend stands out for its focus on sustainability and ethical investments. The returns are competitive too!',
            'author': 'David Chen',
            'role': 'Retired Teacher',
            'image': 'https://randomuser.me/api/portraits/men/33.jpg',
            'rating': 5,
            'date': 'February 3, 2023'
        },
        {
            'id': 5,
            'content': 'The environmental impact metrics helped me understand exactly how my investments are contributing to a healthier planet. Love the transparency!',
            'author': 'Emma Wilson',
            'role': 'Environmental Scientist',
            'image': 'https://randomuser.me/api/portraits/women/22.jpg',
            'rating': 4,
            'date': 'May 17, 2023'
        },
        {
            'id': 6,
            'content': 'As a first-time investor, EcoLend made the process simple and educational. Their customer service team was extremely helpful when I had questions.',
            'author': 'Marcus Taylor',
            'role': 'New Investor',
            'image': 'https://randomuser.me/api/portraits/men/42.jpg',
            'rating': 4.5,
            'date': 'June 9, 2023'
        }
    ]
    
    return render_template('testimonials.html', testimonials=testimonials_data)

@app.route('/logout')
def logout():
    # Clear session
    session.clear()
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    # Check if user is logged in
    # if 'user_id' not in session:
    #     return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/apply_loan', methods=['GET', 'POST'])
def apply_loan():
    if request.method == 'POST':
        # Process loan application
        flash('Loan application submitted successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('apply_loan.html')

@app.route('/my_loans')
def my_loans():
    # Fetch user's loans
    return render_template('my_loans.html')

@app.route('/investment_opportunities')
def investment_opportunities():
    # Fetch available investment opportunities
    return render_template('investment_opportunities.html')

@app.route('/my_investments')
def my_investments():
    # Fetch user's investments
    return render_template('my_investments.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        # Update user profile
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile'))
    return render_template('profile.html')

@app.route('/credit_score')
def credit_score():
    # Show user's credit score and history
    return render_template('credit_score.html')

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        # Update settings
        flash('Settings updated successfully!', 'success')
        return redirect(url_for('settings'))
    return render_template('settings.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/documentation')
def documentation():
    return render_template('documentation.html')

@app.route('/wallet', methods=['GET', 'POST'])
def wallet():
    # Handle wallet operations
    return render_template('wallet.html')

@app.route('/transactions')
def transactions():
    # Show transaction history
    return render_template('transactions.html')

if __name__ == '__main__':
    app.run(debug=True)