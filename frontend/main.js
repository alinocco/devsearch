let loginButton = document.getElementById('login-button')
let logoutButton = document.getElementById('logout-button')

let token = localStorage.getItem('token')

if(token){
    loginButton.remove()
}else{
    logoutButton.remove()
}

logoutButton.addEventListener('click', (e) => {
    e.preventDefault()
    localStorage.removeItem('token')
    window.location = '/home/lina/Documents/SFW/Portfolio/2022.06.09 Django 2021 (Dennis Ivy) - restated/devsearch/frontend/login.html'
})


let projectsUrl = 'http://127.0.0.1:8000/api/projects/'

let getProjects = () => {

    fetch(projectsUrl)
    .then(response => response.json())
    .then(data => {
        console.log(data)
        buildProjects(data)
    })
}

let buildProjects = (projects) => {
    let projectsWrapper = document.getElementById('projects-wrapper')
    projectsWrapper.innerHTML = ''
    
    for (let i = 0; i < projects.length; i++){
        let project = projects[i]
        
        let projectCard = `
                <div class="project--card">
                    <img src="http://127.0.0.1:8000${project.image}" />

                    <div>
                        <div class="card--header">
                            <h3>${project.title}</h3>
                            <strong class="vote--option" data-vote="up" data-project="${project.uuid}" >&#8593;</strong>
                            <strong class="vote--option" data-vote="down" data-project="${project.uuid}" >&#8595;</strong>
                        </div>

                        <i>${project.vote_ratio}% Positive Feedback</i>
                        <p>${project.description.substring(0, 150)}</p>
                    </div>

                </div>
        `
        projectsWrapper.innerHTML += projectCard
    }

    // Add Event Listener
    getVoteEvents()
}

let getVoteEvents = () => {
    let voteButtons = document.getElementsByClassName('vote--option')
    
    for(let i = 0; i < voteButtons.length; i++){
        voteButtons[i].addEventListener('click', (e) => {
            let token = localStorage.getItem('token')

            let vote = e.target.dataset.vote
            let project = e.target.dataset.project

            fetch(`http://127.0.0.1:8000/api/projects/${project}/review/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`
                },
                body: JSON.stringify({
                    'vote': vote,
                    'comment': null,
                })
            })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data)

                getProjects()
            })
        })

    }

}

getProjects()