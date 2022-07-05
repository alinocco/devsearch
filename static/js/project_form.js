// Project Tags Editing

// TODO: 
// Adding Tags
// let inputTag = document.getElementsByName('newtags')[0]

// inputTag.addEventListener('keyup', (e) => {
//     if (e.code === 'Space' || e.code === 'Enter') {
//         let project = e.target.dataset.project
//         let tag = e.target.value.trim()

//         if (tag.length != 0) {
//             fetch('http://127.0.0.1:8000/api/add-tag/', {
//                 method: 'POST',
//                 headers: {
//                 'Content-Type': 'application/json'
//                 },
//                 body: JSON.stringify({'project': project, 'tag': tag})
//             })
//             .then(response => response.json())
//             .then(data => {
//                 console.log("PROJECT:", project)
//                 console.log("TAG:", tag)

//             })
//         }
//     }
// })


// Removing Tags
let tags = document.getElementsByClassName('tag__delete')

  for(let i = 0; i < tags.length; i++){
    tags[i].addEventListener('click', (e) => {
      e.preventDefault()
      let tag = e.target.dataset.tag 
      let project = e.target.dataset.project

      fetch('http://127.0.0.1:8000/api/remove-tag/', {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({'project': project, 'tag': tag})
      })
      .then(response => response.json())
      .then(data => {
        e.target.parentNode.remove()
      })

    })
  }