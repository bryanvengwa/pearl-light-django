const container = document.querySelector('.categories-container')
const footer = document.querySelector('.footer-section')


window.addEventListener('scroll', function(){

    if (window.scrollY >= container.scrollHeight - 100 ){
        if(container.classList.contains('fixed')){
            return
        }else
        container.classList.add('fixed')
    }else if (window.scrollY <= container.scrollHeight + 9000 ){
        
        container.classList.remove('fixed')
    }


})