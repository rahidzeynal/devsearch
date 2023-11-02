let logoutBtn = document.getElementById('logout-btn')
let loginBtn = document.getElementById('login-btn')
console.log("Token is got", loginBtn)


let token = localStorage.getItem('token')
console.log("Token is got: ", token)

if (token) {
    // console.log("Token is got", loginBtn)
    loginBtn.remove()
} else {
    // console.log('Console is null', logoutBtn)
    logoutBtn.remove()
}

logoutBtn.addEventListener('click', (e) => {
    e.preventDefault()
    localStorage.removeItem('token')
    window.location ='file:///C:/Users/rahidz/Desktop/Devsearch/devsearch/frontend/login.html'
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
    let projectsWrapper = document.getElementById('projects--wrapper')
    projectsWrapper.innerHTML = ''
    // console.log('projectsWrapper : ', projectsWrapper)

    for (let i = 0; i < projects.length; i++) {
        let project = projects[i]
        // console.log(project)
        let projectCard =`
            <div class="project--card">
                <img src="http://127.0.0.1:8000${project.featured_image}" />

                <div>
                    <div class="card--header">
                        <h3>${project.title}</h3>
                        <strong class="vote--option" data-vote="up" data-project="${project.id}">&#43;</strong>
                        <strong class="vote--option" data-vote="down" data-project="${project.id}">&#8722;</strong>
                    </div>
                    <i>${project.vote_ratio}% Positive feedback </i>
                    <p>${project.description.substring(0,150)}</p>
                </div>
            </div>
        `

        projectsWrapper.innerHTML += projectCard
    }
    
    addVoteEvents()
    // Add a listener
}


let addVoteEvents = () => {
    let voteBtns = document.getElementsByClassName('vote--option')
    // console.log(voteBtns)
    for (let i = 0; i < voteBtns.length; i++) {
        voteBtns[i].addEventListener('click', (e) => {
            let token = localStorage.getItem('token') 
            //'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxNDI4NTQxLCJpYXQiOjE2OTg4MzY1NDEsImp0aSI6ImIwODY4MmU5NzFhZjRlNTg4NjdmOTAxZmJlMzVkYjVmIiwidXNlcl9pZCI6MX0.9cMnN9GmmTz0cmYjYxaI36Id4PZn8a_opwHPHyUCZQQ'
            // console.log('Vote was clicked: ', i)
            let vote = e.target.dataset.vote
            let project = e.target.dataset.project
            // console.log('Project: ', project, ' Vote: ', vote)
            fetch(`http://127.0.0.1:8000/api/projects/${project}/vote/`, {
                method: 'POST',
                headers: {
                    'Content-Type':'application/json',
                    Authorization: `Bearer ${token}`
                },
                body:JSON.stringify({'value':vote})
            })

            .then(response => response.json())
            .then(data => {
                console.log('Success: ', data)
                getProjects()
            })
            
        })
    }
}


getProjects()