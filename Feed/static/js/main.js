const burger = document.querySelector('#burger')
const menu = document.querySelector('#mobile-menu')
const profilebtn = document.querySelector('#profile')
const profilemenu = document.querySelector('#profile-menu')

burger.addEventListener('click', () => {
    if (menu.classList.contains('hidden')){
        menu.classList.remove('hidden');
    } else {
        menu.classList.add('hidden')
    }
})

profilebtn.addEventListener('click', () => {
    if (profilemenu.classList.contains('hidden')){
        profilemenu.classList.remove('hidden');
    }else{
        profilemenu.classList.add('hidden')
    }
})