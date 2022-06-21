
// Get Search Form and Pagination Links
let searchForm = document.getElementById("searchForm")
let pageLinks = document.getElementsByClassName("page-link")

// Ensure Search Form exists
if(searchForm){
    for(let i = 0; i < pageLinks.length; i++){
        pageLinks[i].addEventListener('click', function(e){
            e.preventDefault()
            
            // Get the data-page attribute
            let page = this.dataset.page
            
            // Add hidden field to Search Form
            searchForm.innerHTML += `<input value=${page} name="page" hidden />`

            // Submit Search Form
            searchForm.submit()
        })
    }
}