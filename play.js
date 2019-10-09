// const items = [95, 262, 2015, 2009]
// const noop = (value) => value;

// for ( let i = 0; i< items.length; i++){
//     noop(items[i])
// }

// let value = 32;
// const result = value << 1

// const obj = {
//     value: 2009
// }

// const func = function (){
//     this.value = 262;
// }

// func.call(obj)
// const result = obj.value
// let result = 2009;

// try{
//     result = 262 / 0;
// }
// catch(e){
//     result = 0 / 262
// }

// const params = [1,2,3,4,5];

// const result = Math.max.apply(10, params);

// function func (a,b){
//     "use strict";
//     a = 262;
//     b = 95;
//     const result = arguments[1]
//     return result
// };

// let value = 10;
// const promise = new Promise((resolve) =>{
//     value = 20;
//     resolve(30)
// })

// const result = value;

// const object = new Object();
// const proto = Object.getPrototypeOf(object);

// const result = proto instanceof Object


// const array = [1,2,3,4,5]
// const result = array.fill(2,0,3).join("");

// const obj = {
//     name: "Javascript"
// };

// Object.seal(obj);
// obj.name = "EcmaScript"
// const result = obj.name

// const push = Array.prototype.push;
// const first = [2009, 95]
// const second = [95,2009]

// const result = push.apply(first, second)

// const result = null + [0,[1,2]][1][1];


// console.log(result)



/*****************Javascript Change on Url Parameters ************************/


// let url_param = "https://www.hiber.com/who-we-are?utm_campaign=t1-a1-c1";

// let url_split = url_param.split("?")[1].split("=")[0];

// if (typeof(url_split ) === 'string' && url_split === 'utm_campaign'){
//     let split_hero_title = url_param.split("=")[1]
//     let url_num;
  
//     if(split_hero_title.includes("1")){
//         url_num = 1
     
//     }
//     else if(split_hero_title.includes("2")){
//         url_num = 2
//     }
//     else if(split_hero_title.includes("3")){
//         url_num = 3
//     }

//     switch(url_num){
//         case 1:
//         document.querySelector(".m-hero_title").innerHTML = "Hero Title1";
//         document.querySelector(".m-hero_description").innerHTML = "Hero Description1";
//         break;

//         case 2:
    
//         document.querySelector(".m-hero_title").innerHTML = "Hero Title2";
//         document.querySelector(".m-hero_description").innerHTML = "Hero Description2";
//         break;


//         case 3:
//         document.querySelector(".m-hero_title").innerHTML = "Hero Title3";
//         document.querySelector(".m-hero_description").innerHTML = "Hero Description3";
//         break;
//         default:
//         console.log("Hero Description")
//     }

    
// }

// else{
//     console.log("url parameter does not exist")
// }

 
// /*****************Javascript Data Parsing  ************************/

// let LADCart = [
// {
// "id":1,
// "productName":"black water rush",
// "productPrice":149,
// "productQuantity":5    
// },
// {
//     "id":2,
//     "productName":"hall of faces",
//     "productPrice":1000,
//     "productQuantity":3    
//     },

// {
//     "id":3,
//         "productName":"ice dragon",
//         "productPrice":149,
//         "productQuantity":2    
//      },
 
// {
//     "id":4,
//         "productName":"ice dragon",
//         "productPrice":149,
//         "productQuantity":2    
//      },


// {
//     "id":5,
//         "productName":"ice dragon",
//         "productPrice":149,
//         "productQuantity":2    
//      },



// {
//     "id":6,
//         "productName":"ice dragon",
//         "productPrice":149,
//         "productQuantity":2    
//      },
// ]
  

// function groupBy(objectArray, property) {
//     return objectArray.reduce(function (acc, obj) {
//       var key = obj[property];
//       if (!acc[key]) {
//         acc[key] = [];
//       }
      
//     let total_price = 0
//     if(acc[key].length < 3){

//         acc[key].push(obj);
//         acc[key].forEach(element => {
//             qty_price = element.productPrice * element.productQuantity
//             acc[key]['quantity_price'] = qty_price
          
//         })  
//     }  

//     else{
//         return `Only Maximum of 3 identical products can be added for ${obj['productName']}`
//     }
    
//        let acc_len = Object.keys(acc)
//        for (let a of acc_len){
//            if(typeof(acc[a]['quantity_price']) !== 'undefined'){
//            total_price += acc[a]['quantity_price']
//            }
//        }
  
//       acc['total_price'] = total_price

//       return acc;
//     }, {});
//   }

//   var addCart = groupBy(LADCart, 'productName');



console.log(typeof undefined)



// "Principal": {
//     "AWS": "arn:aws:iam::362750386222:user/springs-owner"
// },