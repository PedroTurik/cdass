#![allow(non_snake_case)]

use std::fs;


fn count_damage(laser: &[Mode]) -> i32{
    let mut total = 0;
    let mut cur_dmg = 1;
    laser.iter().for_each(|c| {
        match *c {
            Mode::Charge => cur_dmg *= 2,
            Mode::Shot(_) => total += cur_dmg,
            _ => {panic!()}
        }
    });

    total

}


enum Mode {
    Charge, Shot(usize)
}

fn main() {
    let binding = fs::read_to_string("input.txt").unwrap();
    let mut inp = binding.split('\n');

    let shield: i32 = inp.next().unwrap().parse().unwrap();
    let mut cur_dmg = 1;
    let laser: Vec<Mode> = inp.next().unwrap().chars().map(|c| if c == 'C' {cur_dmg *= 2; Mode::Charge} else {Mode::Shot(cur_dmg)} ).collect();

    
    


}
