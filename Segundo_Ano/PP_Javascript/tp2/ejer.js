//Escribe un programa que filtre los números pares de un array utilizando un bucle for y la función push().
let numeros = [1,2,3,4,5,6,7,8,9]
let numerosPares = []
for (let i=0; i < numeros.length; i++){
    if (numeros[i] % 2 === 0){
        numerosPares.push(numeros[i]);
    }
}
console.log(numerosPares)

//Escribe un programa que elimine todos los números negativos de un array utilizando un bucle for y la función splice().

let numeros = [1,-2,3,-4,5,-6,7,-8]
for (i=0; i < numeros.length; i++){
    if (numeros[i] < 0){
        numeros.splice(i-1,1);
}

}
console.log(numeros)

//escribe un programa que elimine todos llos numeros impares del 1 al 20
//con while y pop()
let numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
let numerosPares = []

while (numeros.length > 0){
    let borrar = numeros.pop()
    if (borrar % 2 === 0){
        numerosPares.push(borrar)
    }
}
console.log(numerosPares)