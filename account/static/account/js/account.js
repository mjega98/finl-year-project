window.onload = () => {
    let messages = document.querySelectorAll('.messages')

    messages.forEach((element, index) => {
        element.style.setProperty('--index', index)
        element.querySelector('i').onclick = ()=>element.remove()
        setTimeout(() => { element?.remove?.() }, 5000 + (index * 1000))
    })
}
