extern crate wasm_bindgen;

use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn check_password(s: String) -> bool {
    if s.len() != 30 {
        return false;
    }

    let s = s.as_bytes();
    // th3_an5w3r_15_n0t_42_but_31337

    if s[9] != 114 { return false;}
    if s[25] != 51 { return false;}
    if s[2] != 51 { return false;}
    if s[4] != 97 { return false;}
    if s[7] != 119 { return false;}
    if s[19] != 50 { return false;}
    if s[18] != 52 { return false;}
    if s[8] != 51 { return false;}
    if s[3] != 95 { return false;}
    if s[20] != 95 { return false;}
    if s[6] != 53 { return false;}
    if s[26] != 49 { return false;}
    if s[15] != 48 { return false;}
    if s[27] != 51 { return false;}
    if s[16] != 116 { return false;}
    if s[24] != 95 { return false;}
    if s[17] != 95 { return false;}
    if s[22] != 117 { return false;}
    if s[28] != 51 { return false;}
    if s[11] != 49 { return false;}
    if s[12] != 53 { return false;}
    if s[5] != 110 { return false;}
    if s[0] != 116 { return false;}
    if s[10] != 95 { return false;}
    if s[29] != 55 { return false;}
    if s[13] != 95 { return false;}
    if s[21] != 98 { return false;}
    if s[14] != 110 { return false;}
    if s[1] != 104 { return false;}
    if s[23] != 116 { return false;}

    true
}