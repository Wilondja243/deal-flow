

window.addEventListener('DOMContentLoaded', (e)=>{
    const links = document.querySelectorAll('.link');

    links.forEach(link => {
        if(window.location.href === link.href){
            console.log(window.location.href)
            link.classList.add('active-link');
        }
    })

    // Sélection des élements du formulaire activity_form.html
    const form = document.getElementById('activityForm');
    const tabButtons = document.querySelectorAll('.tab-button');

    if(form){
        function setActiveTab(type) {

            const typeFields = {
                task: document.querySelector('.task-date-row'),
                call: document.querySelector('.call-outcome-row'),
                email: document.querySelector('.email-subject-row')
            };

            // Mise à jour des boutons
            tabButtons.forEach(btn => {
                btn.classList.remove('active');
                if (btn.getAttribute('data-type') === type) {
                    btn.classList.add('active');
                }
            });

            // Mise à jour de l'affichage des champs spécifiques
            form.setAttribute('data-active-type', type);
            
            for (const fieldType in typeFields) {
                if (typeFields[fieldType]) {
                    typeFields[fieldType].style.display = (fieldType === type) ? 'flex' : 'none';
                }
            }
            
            // Mise à jour du bouton d'action et du sujet
            const submitButton = form.querySelector('.btn-primary');
            if (type === 'task') {
                submitButton.innerHTML = '<i class="bi bi-check2-square"></i> Planifier la Tâche';
            } else if (type === 'call') {
                submitButton.innerHTML = '<i class="bi bi-telephone-fill"></i> Enregistrer l\'Appel';
            } else if (type === 'email') {
                submitButton.innerHTML = '<i class="bi bi-envelope-fill"></i> Enregistrer l\'E-mail';
            }
        }

        tabButtons.forEach(button => {
            button.addEventListener('click', function() {
                setActiveTab(this.getAttribute('data-type'));
            });
        });

        setActiveTab('task');
    }
})