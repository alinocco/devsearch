let form = document.getElementById('login-form')

form.addEventListener('submit', (e) => {
    e.preventDefault()
    
    let formData = {
        'username': form.username.value,
        'password': form.password.value,
    }

    console.log(formData)

    fetch('http://127.0.0.1:8000/api/users/token/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        if (data.access){
            localStorage.setItem('token', data.access)
            window.location = '/home/lina/Documents/SFW/Portfolio/2022.06.09 Django 2021 (Dennis Ivy) - restated/devsearch/frontend/main.html'
        } else {
            alert('You have submitted a wrong username or password.')
        }

    })
})