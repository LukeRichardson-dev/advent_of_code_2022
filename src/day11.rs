use std::{rc::Rc, cell::RefCell, ops::Mul};

#[derive(Debug, Hash, PartialEq, Eq, Clone)]
pub enum Operation {
    Add(u128),
    Mul(u128),
    Pwr,
}

impl Operation {
    pub fn apply(&self, a: u128) -> u128 {
        match &self {
            Self::Add(b) => a + b,
            Self::Mul(b) => a * b,
            Self::Pwr => a * a,
        }
    }
}

#[derive(Debug, PartialEq, Eq, Clone)]
pub struct Monke {
    items: Vec<u128>,
    operation: Operation,
    pub m: u128,
    left: usize,
    right: usize,
    pub count: usize,
}

impl Monke {
    
    pub fn new(
        items: Vec<u128>,
        operation: Operation,
        m: u128,
        left: usize,
        right: usize,
    ) -> Self {
        Self {
            items,
            operation,
            m,
            left,
            right,
            count: 0
        }
    }


    pub fn inspect(&mut self, monkes: &Vec<RefCell<Monke>>, max: u128) {
        self.count += self.items.len();

        while let Some(i) = self.items.pop() {
            let c = self.operation.apply(i) % max;
            
            if c % self.m == 0 {
                monkes[self.left].borrow_mut().items.push(c);
            } else {
                monkes[self.right].borrow_mut().items.push(c);
            }
        }

    }
}

fn test_monke() -> Vec<RefCell<Monke>> {
    let mut test_monkes: Vec<RefCell<Monke>> = vec![];
    test_monkes.push(
        RefCell::new(Monke::new(
            vec![79, 98],
            Operation::Mul(19), 
            23,
            2,
            3
        ))
    );
    test_monkes.push(
        RefCell::new(Monke::new(
            vec![54, 65, 75, 74],
            Operation::Add(6),
            19, 
            2, 
            0
        ))
    );
    test_monkes.push(
        RefCell::new(Monke::new(
            vec![79, 60, 97],
            Operation::Pwr, 
            13, 
            1, 
            3
        ))
    );
    test_monkes.push(
        RefCell::new(Monke::new(
            vec![74],
            Operation::Add(3), 
            17, 
            0, 
            1
        ))
    );

    test_monkes
}

fn real_monke() -> Vec<RefCell<Monke>> {
    let mut test_monkes: Vec<RefCell<Monke>> = vec![];
    test_monkes.push(
        RefCell::new(Monke::new(
            vec![85, 77, 77],
            Operation::Mul(7),
            19, 6, 7
        ))
    );
    test_monkes.push(
        RefCell::new(Monke::new(
            vec![80, 99],
            Operation::Mul(11),
            3, 3, 5
        ))
    );
    test_monkes.push(
        RefCell::new(Monke::new(
            vec![74, 60, 74, 63, 86, 92, 80],
            Operation::Add(8),
            13, 0, 6
        ))
    );
    test_monkes.push(
        RefCell::new(Monke::new(
            vec![71, 58, 93, 65, 80, 68, 54, 71],
            Operation::Add(7),
            7, 2, 4
        ))
    );
    test_monkes.push(
        RefCell::new(Monke::new(
            vec![97, 56, 79, 65, 58],
            Operation::Add(5),
            5, 2, 0
        ))
    );
    test_monkes.push(
        RefCell::new(Monke::new(
            vec![77],
            Operation::Add(4),
            11, 4, 3
        ))
    );
    test_monkes.push(
        RefCell::new(Monke::new(
            vec![99, 90, 84, 50],
            Operation::Pwr,
            17, 7, 1
        ))
    );
    test_monkes.push(
        RefCell::new(Monke::new(
            vec![50, 66, 61, 92, 64, 78],
            Operation::Add(3),
            2, 5, 1
        ))
    );

    test_monkes
}

fn cmb(monkes: Vec<RefCell<Monke>>) {
    let max = monkes.iter().map(|v| v.borrow().m).fold(1, |acc, v| v * acc);
    for _ in 0..10000 {
        for i in &monkes {
            i.borrow_mut().inspect(&monkes, max);
        }
    }
    
    let counts: Vec<usize> = monkes.iter().map(|v| v.borrow().count).collect();
    let a = counts.iter().max().unwrap();
    let b = counts.iter().filter(|x| *x != a).max().unwrap();

    println!("{} * {} = {}", a, b, a * b);
}

pub fn run() {
    let test_monkes = test_monke();
    cmb(test_monkes);

    let real = real_monke();
    cmb(real);
}