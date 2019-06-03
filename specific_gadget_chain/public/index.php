<?php

include 'flag.php';

$item_files = ['items/1','items/2','items/3','items/4','items/5'];

class User
{
    public $username;
    public $password_hash;
    public $firstname;
    public $lastname;
    public $cart;
    private $role;

    function __construct($username, $password, $firstname, $lastname, $cart)
    {
        $this->username = $username;
        $this->password_hash = hash('sha512', $password.'4JQQwT3W');
        $this->firstname = $firstname;
        $this->lastname = $lastname;
        $this->cart = $cart;
        $this->role = 'user';
        $this->save();
    }

    function __destruct()
    {
        $this->cart->delete();
        unlink('../users/'.$this->username);
    }

    function save()
    {
        $user = [
            'username' => $this->username,
            'password_hash' => $this->password_hash,
            'firstname' => $this->firstname,
            'lastname' => $this->lastname,
            'cart' => $this->cart,
            'role' => $this->role,
            'spbctf' => 'rulez'
        ];

        file_put_contents('../users/'.$this->username, serialize($user));
    }

    function setCart($filename)
    {
        $this->cart = $filename;
        $this->save();
    }

    function show()
    {
        echo file_get_contents('../users/'.$this->username);
    }
    
}

class Item
{
    public $info;
    public $price;

    function __construct($info, $price)
    {
        $this->info = $info;
        $this->price = $price;
    }
    
    function show()
    {
        echo file_get_contents($this->info);
    }
}

class Cart
{
    public $defaultCart = '../carts/empty';
    public $filename;
    public $items = array();

    function delete()
    {
        foreach($this->items as $item)
        {
            echo 'Deleting Item :'.$item->show();
            unset($item);
        }
        unlink($this->filename);
    }

    function __construct($username)
    {
        $this->filename = '../carts/'.$username;
        $this->save();
    }

    function save()
    {
        file_put_contents($this->filename, serialize($this));
    }

    function addItem($item)
    {
        $this->items[] = $item;
    }
}

if(!isset($_GET['serialized']))
{
    highlight_file(__FILE__);
}
else
{
    unserialize($_GET['serialized']);
}
