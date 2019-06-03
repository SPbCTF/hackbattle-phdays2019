<?php

session_start();
$pdo = new PDO('mysql:host=db;dbname=battles', 'root', 'root');
$pdo->exec("set names utf8");

if (isset($_SESSION['login'])) {
    if ($_SESSION['is_raffle'] && isset($_GET['raffle'])) {
        $raffleCoin = rand(1,5);
        $query = $pdo->prepare('UPDATE racecondition SET coin=coin+:coin WHERE login=:login');
        $query->bindParam(':login', $_SESSION['login'], PDO::PARAM_STR);
        $query->bindParam(':coin', $raffleCoin, PDO::PARAM_INT);
        $query->execute();
        $_SESSION['is_raffle'] = 0;
        header('Location: ./');
        exit;
    }
    $query = $pdo->prepare('SELECT * FROM racecondition WHERE login=:login');
    $query->execute([':login' => $_SESSION['login']]);
    $user = $query->fetchObject();
    if ($_SESSION['is_raffle']) {
        echo '<a href="./?raffle=1">Начать розыгрыш</a><br>';
    }
    echo 'Логин:' . $user->login . '<br>';
    echo 'Монетки:' . $user->coin . '<br>';
    if ($user->coin > 5) {
        echo 'MnePlevatb9Krasav4eg';
    }
    exit;
} else {
    if (isset($_POST['login']) && isset($_POST['password'])) {
        if ($_POST['login'] && $_POST['password']) {
            $login = $_POST['login'];
            $password = $_POST['password'];
            $query = $pdo->prepare('SELECT login FROM racecondition WHERE login=:login');
            $query->execute([':login' => $login]);
            if (!$query->rowCount()) {
                sleep(3); // TODO strong crypt
                $query = $pdo->prepare('INSERT INTO racecondition SET login=:login, password=:password');
                $query->execute([':login' => $login, ':password' => $password]);
                $_SESSION['login'] = $login;
                $_SESSION['is_raffle'] = 1;
                header('Location: ./');
                exit;
            } else {
                $message = 'Такой пользователь уже есть';
            }
        } else {
            $message = 'Логин пароль не могут быть пустые';
        }
    }
}
?>
<form method="post" action="./">
    <p>
        Логин <input type="text" name="login">
    </p>
    <p>
        Пароль <input type="text" name="password">
    </p>
    <input type="submit" value="Регистрация">
</form>
<?= (isset($message))?$message:'' ?>
