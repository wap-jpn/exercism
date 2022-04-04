/* https://exercism.org/tracks/rust/exercises/leap
 * Philip Woite
 */
/* References
 * https://doc.rust-lang.org/std/keyword.if.html
 * https://stackoverflow.com/a/30355516
 * https://doc.rust-lang.org/std/keyword.mut.html
 * https://doc.rust-lang.org/reference/comments.html
 * https://riptutorial.com/rust/example/1248/advanced-usage-of-println-
 */

use text_io::read;

fn main() {
    println!("Enter the year to test for leapyear");
    let year: i32 = read!();
    let mut leap = "No";

    if year%4==0 {
        if year%100>0 {
            leap = "Yes"}
        else { if year%400==0 {
            leap = "Yes"}
            else {
                leap = "No"}
        }
    }
    println!("Is {} a leapyear? - {}",year,leap);
}
