use std::io;

fn main() {
    let mut inp: String = "".to_owned();
    let stdin = io::stdin();
    stdin.read_line(&mut inp).unwrap();
    
    let mut ans = 0;
    let mut last = 0;
    let mut tmp_sum = 0;

    let my_iter: Vec<i32> = inp.split(",").map(|x| x.parse().unwrap()).collect();
    for h in &my_iter{
        if *h < last{
            tmp_sum += last - *h;
        }
        else{
            ans += tmp_sum;
            tmp_sum = 0;
            last = *h;
        }
    }

    let first_last = last;
    last = 0;
    tmp_sum = 0;

    for h in my_iter.iter().rev(){
        if *h == first_last{
            ans += tmp_sum;
            break;
        }

        if *h < last{
            tmp_sum += last - h;
        }
        else{
            ans += tmp_sum;
            tmp_sum = 0;
            last = *h;
        }  
    }

    println!("{ans}")

}
