const menubar = document.querySelector('.menubar');
const left_sidebar = document.querySelector('.left_side');
const righ_sidebar = document.querySelector('.right_side');
const link_text = document.querySelectorAll('.active');
const form = document.querySelector('#search-form');
const alert_diplay = document.querySelector('#alert');
const cross_button = document.querySelector('#cross');
const profile_icon = document.querySelector('.user-profile-icon')
const profile_slider = document.querySelector('#profile');


// profile icon toggle script 
if (profile_icon) {

    profile_icon.addEventListener('click', () => {
        profile_slider.classList.toggle('profile-user')
    })
    
    
}


// menubar side script 
menubar.onclick = () => {
    link_text.forEach((item) => {
        item.classList.toggle('hide')
    })
    if (left_sidebar && righ_sidebar) {

        left_sidebar.classList.toggle('new-width');
        righ_sidebar.classList.toggle('right-width')
    }
}

// alert_diplay show script 
if (alert_diplay) {

    setTimeout(() => {

        alert_diplay.classList.add('hide-message')
    }, 2000)
    cross_button.addEventListener('click', () => {
        alert_diplay.classList.add('hide-message')

    })
}

