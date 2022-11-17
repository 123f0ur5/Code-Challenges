let ai_score = 0
let ai_cards = ""
let score = 0
let cards = ""
let user_score = 0
let computer_score = 0
let tie = 0
let message_el = document.getElementById('message')
let cards_el = document.getElementById('cards')
let score_el = document.getElementById('score')
let status_el = document.getElementById('status')
let winlose_el = document.getElementById('winlose')
let user_score_el = document.getElementById('user-score')
let computer_score_el = document.getElementById('computer-score')
let tie_el = document.getElementById('ties')
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
            user_score += 1
            update_score()
        } else if (ai_score == score && score <= 21 && ai_score <= 21) {
            winlose_el.textContent = "It's a TIE :|"
            tie += 1
            update_score()
        } else {
            winlose_el.textContent = "You lose :("
            computer_score += 1
            update_score()
        }
    }
}

function update() {
    if (score == 21) {
        stop()
    } else if (score > 21) {
        winlose_el.textContent = "You lose :("
        computer_score += 1
        update_score()
    }
    cards_el.textContent = "Cards: " + cards
    score_el.textContent = "Score: " + score
}

function update_score(){
    console.log(user_score, computer_score, tie)
    user_score_el.textContent = "User: " + user_score
    computer_score_el.textContent = "Computer: " + computer_score
    tie_el.textContent = "Tie: " + tie
}