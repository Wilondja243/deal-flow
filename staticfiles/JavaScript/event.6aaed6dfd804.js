window.addEventListener('DOMContentLoaded', (e)=>{
    const links = document.querySelectorAll('.link');

    links.forEach(link => {
        if(window.location.href === link.href){
            console.log(window.location.href)
            link.classList.add('active-link');
        }
    })
})