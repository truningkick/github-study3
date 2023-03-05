import UIKit
//-----------------------------------------------------
/*
 // 변수,상수와 if/else
 var greeting = 10 //var:변수, let:상수

 // if else문
var value : String = greeting == 10 ? "10이다" : "10이 아니다"
print("value:",value)

if (value == "10이 아니다")
{
    print("not 10")
}
else
{
    print("10")
}
*/
//-----------------------------------------------------
//배열 array
//콜렉션:데이터를 모아둔 것, 배열,셋,딕셔너리,튜플
/*
var  myArray : [String] = ["가","나","다","라"]
var  myArray2 : [Int] = [1,2,3,4,5,6,7,8]

print(myArray)
print(myArray2)
*/
//-----------------------------------------------------
// for문, where함수(특정 조건 추가)
/*
for index in 0..<5 where index%2 == 0
{
    print("짝수 : \(index)")
}

var randomints : [Int] = [Int]()
for _ in 0..<25
{
    let randomN = Int.random(in:1...13)
    randomints.append(randomN)
}
print("결과: \(randomints)")
*/
//-----------------------------------------------------
// 옵셔널 *값이 있나? 없나?;; 모르겠노
// type(of:)함수 *변수의 자료형 확인,
// String(describing:) *문자열로 변환
/*
var someVariable:Int? = nil
var x:Any
var y:Any
 
if someVariable == nil{someVariable = 13}
print("RESULT: \(String(describing: someVariable))")
x = someVariable
y = String(describing: someVariable)

print("someV타입:\(type(of:someVariable))\n", "x타입:\(type(of:x))\n", "y타입:\(type(of:y))")
//언랩핑 ver1
if let otherVariable = someVariable //값이 있을 때 실행
{
    print("언래핑 되었다 -> 값이 있다 -> OtherVariable: \(otherVariable),","\t타입: \(type(of: otherVariable))")
}
else{ print("값이 없다")}
//언랩핑 ver2
//함수호출 및 guard else *참이 되어야 계속, 거짓일경우 종료(유사if else)
// if let : 조건문이 nil 이면 실행
// *지역변수로만 사용 가능, 옵셔널 값이 nil인지 확인하고 2분기로 작업 가능
// guard let : guard 안의 조건문이 참(true)이 아니면 else문 실행
// *전역변수로 사용 가능, 조건이 trued일 때 계속 실행, 조건이 falsed일 때 탈출문(break, continue등) 필요

var firstV : Int? = 33 //옵셔널 변수 선언 ? 사용
var secondV : Int? = 77
print("first value: \(firstV)", "\nsecond value: \(secondV)")

unwrap(firstV)
unwrap(secondV)

func unwrap(_ parameter:Int?)
{
    print("unwrap() called !")
    guard let unWrappedParam = parameter
    else
    {
        return
    }
    print("unWrappedParam: \(unWrappedParam),\t","type: \(type(of:unWrappedParam))") //guard 생성 변수 전역변수 활용 가능
}
*/
//-----------------------------------------------------
//스트럭트 : 주소(참조)형 아니고, 값 복사
/*
struct peoplefeature
{
    var name : String
    var height : Int
    var weight : Int
}

var kim = peoplefeature(name: "kimjaehyoung", height: 175, weight: 73)
var park = kim

print("원본 - kim name : \(kim.name) \theight : \(kim.height) \tweight : \(kim.weight)")   //
park.name = "parkchangheok"; park.height = 192; park.weight = 80
print("원본 - kim name : \(kim.name) \theight : \(kim.height) \tweight : \(kim.weight)")
print("수정 - park name : \(park.name) \theight : \(park.height) \tweight : \(park.weight)")
*/
//-----------------------------------------------------
// 클래스 : 참조형(주소) 수정시 원본에 영향
/*
class profile
{
    var name : String
    var height : Int
    var weight : Int
    init(name:String, height:Int, weight:Int )
    {
        self.name = name
        self.height = height
        self.weight = weight
    }
}

var kimkim = profile(name:"김재형", height: 175, weight: 73)
var parkpark = kimkim

print("원본 - kimkim name : \(kimkim.name) \theight : \(kimkim.height) \tweight : \(kimkim.weight)")
parkpark.name = "parkchangheok"; parkpark.height = 192; parkpark.weight = 80
print("원본 - kimkim name : \(kimkim.name) \theight : \(kimkim.height) \tweight : \(kimkim.weight)")
print("수정 - parkpark name : \(parkpark.name) \theight : \(parkpark.height) \tweight : \(parkpark.weight)")
*/
//-----------------------------------------------------
//function 그리고 프로퍼티 get, set / willSet, didSet
//프로퍼티 옵저버: willset, didset : 프로퍼티 값 변경 전, 후 감지 및 수행
//ex: 스코어판. 주로 갱신값 보여줄 때 많이 사용함.
/*
//function
func myfunc1(name:String) -> String         //호출시 매개변수 name
{
    return "Hello my name is \(name)."
}
func myfunc2(with name:String) -> String    //호출시 매개변수 with
{
    print(name)
    return "Hello my name is \(name)."
}
func myfunc3(_ name:String) -> String       //호출시 매개변수 이름 없음
{
    print(name)
    return "Hello my name is \(name)."
}
print("\(myfunc1(name: "김재형"))\n", "\(myfunc2(with: "박예빈"))\n", "\(myfunc3("임한주"))" )
print(myfunc1(name: "노유진"), myfunc2(with: "이혜미") )

//프로퍼티 옵저버
var myage = 0
{
    willSet
    { print("값 설정 예정.\t 나이:\(myage)") }
    didSet
    { print("값 설정 됐음.\t 나이:\(myage)") }
}

print("나이: \(myage)")
myage = 26
print("나이: \(myage)")
*/
//-----------------------------------------------------
//제네릭 <T> 어떤 자료형이든 들어올 수 있도록 설정
/*
struct friend
{
    var name : String
}

struct myarray<T>
{
    var elements = [T]()     //매개변수
    init(_ elements: [T])    //생성자 메소드
    {
        self.elements = elements
    }
}

var myIntarray = myarray([1,2,3,4])
print("myIntarray : \(myIntarray)")
var myStrarray = myarray(["버","텨","인"])
print("myIntarray : \(myStrarray)")

let firstF = friend(name:"재형")
let secondF = friend(name:"예빈")
let thirdF = friend(name:"한주")

var myFriendarray = myarray([firstF,secondF,thirdF])
print("myFriendarray : \(myFriendarray)")

//-----------------------------------------------------
//클로저
