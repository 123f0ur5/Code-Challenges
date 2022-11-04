let ai_score = 0
let ai_cards = ""
let score = 0
let cards = ""
let message_el = document.getElementById('message')
let cards_el = document.getElementById('cards')
let score_el = document.getElementById('score')
let status_el = document.getElementById('status')
let winlose_el = document.getElementById('winlose')
let started = false

function start() {
    started = true
    status_el.textContent = ""
    winlose_el.textContent = ""
    ai_score = 0
    score = 0
    cards = ""
    let card = Math.floor(Math.random() * 11) + 1
    message_el.textContent = "Your starting card is: " + card
    score += card
    cards +=  card
    document.getElementById('stop').style.display="inline"
    update()
}

function new_card(){
    if (score < 21 && started === true) {
        let card = Math.floor(Math.random() * 11) + 1
        message_el.textContent = "Your new card is: " + card
        score += card
        cards += " - " + card
    }
    update()
}

function stop(){
    if (score <= 21) {
        if (score != 21) {
            status_el.textContent = "Your final score is: " + score
        } else {
            status_el.textContent = "YOU GOT BLACKJACK!!"
        }
        while (ai_score < 17){
            ai_score += Math.floor(Math.random() * 11) + 1
        }
        message_el.textContent = "Computer score is: " + ai_score
        if (ai_score > 21 || ai_score < score){
            winlose_el.textContent = "You WIN!!"
        } else if (ai_score == score && score <= 21 && ai_score <= 21) {
            winlose_el.textContent = "It's a TIE :|"
        } else {
            winlose_el.textContent = "You lose :("
        }
    }
}

function update() {
    if (score == 21) {
        stop()
    } else if (score > 21) {
        winlose_el.textContent = "You lose :("
    }
    cards_el.textContent = "Cards: " + cards
    score_el.textContent = "Score: " + score
}