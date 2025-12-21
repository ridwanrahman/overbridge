use std::collections::HashMap;

pub(crate) fn two_sums(arr_of_integers: Vec<i32>, target: i32) -> Vec<i32> {
    let mut map: HashMap<i32, usize> = HashMap::new();

    for (index, &num) in arr_of_integers.iter().enumerate() {
        let difference: i32 = target - &num;
        if let Some(&prev_index) = map.get(&difference) {
            println!("the final result is [{}, {}]", prev_index, index);
            return vec![prev_index as i32, index as i32];
        }
        map.insert(num, index);
    }
    vec![]
}