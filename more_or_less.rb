
def boas_vindas
    puts "Welcome to game"
    puts "What's your name?"
    name = gets
    puts "\n\n\n\n\n"
    puts "We will begin with you, " + name
end

def sorteia_numero_secreto
    puts "Choosing a secret number between 0 and 200 ..."
    #puts "Escolhendo um número secreto entre 0 e 200..."
    number_secret = 175
    puts "Chosen ... How about guessing our secret number today? "    
    return number_secret
end

def pede_numero(attempt, limite_tentativas)
    puts "\n\n\n\n"
    puts "Attempt " + attempt.to_s + " of " + limite_tentativas.to_s
    puts "Enter with the number"
    kick = gets
    puts "Did he get it right? You kicked #{kick}"
    return kick.to_i
end

def verifica_acerto(number_secret, kick)
    if hit
        puts "Hit!!"
        return true;
    end
    #puts "Missed!!" 
    bigger = number_secret.to_i > kick
    if bigger
        puts "The secret number is bigger!"         
    else
        puts "The secret number is smaller!"
    end
    return false;
end

boas_vindas
number_secret = sorteia_numero_secreto
puts "\n\n\n\n"

limite_tentativas = 3
for attempt in 1..limite_tentativas
    kick = pede_numero(attempt, limite_tentativas)
    hit = number_secret.to_i == kick
    break if(verifica_acerto(number_secret, kick))
        #break 
end