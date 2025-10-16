
function dropDown(){
    const triggers = document.querySelectorAll(".dropdown-trigger");
    triggers.forEach(trigger => {
        trigger.addEventListener('click', (e) => {
            e.stopPropagation()
            const wrapper = trigger.closest(".dropdown-wrapper");
            const dropDownMenu = wrapper.querySelector(".dropdown");
            dropDownMenu.classList.toggle("toggle-dropdown")
        })
    })

    document.addEventListener('click', (e) =>{
        if(!e.target.closest(".dropdown-wrapper")){
            document.querySelectorAll(".dropdown").forEach(menu =>{
                menu.classList.remove("toggle-dropdown");
            })
        }
    })
}


window.addEventListener('DOMContentLoaded', (e)=>{
    const links = document.querySelectorAll('.link');

    links.forEach(link => {
        if(window.location.href === link.href){
            console.log(window.location.href)
            link.classList.add('active-link');
        }
    })

    dropDown()
})