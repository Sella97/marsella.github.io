<!DOCTYPE html>>
    <head>
        <title>FORM PENDAFTARAN</title>
    </head>
    <h1>FORM PENDAFTARAN</h1>
    <form action="datapendaftaran.php" method="POST">
        <br>Silahkan Melakukan Pendaftaran dengan mengisi Form di bawah ini dengan lengkap.
    <table border="0" width="500">
        <tr>
        <td>Nama Anak : </td>
        <td></td>
        <td><input type="text" name="name" size="22" placeholder="Masukan Nama Anda"></td>
    </tr>
    <tr>
        <td>Sex : </td>
        <td></td>
        <td><input type="radio" name="sex" value="Laki - Laki">Laki-Laki <input type="radio" name="gender" value="Perempuan">Perempuan</td>
    </tr> 
    <tr>
        <td>Tempat Lahir : </td>
        <td></td>
        <td><input type="text" name="place" size="22" placeholder="Masukan Tempat Lahir Anda"></td>
    </tr>
    <tr>
     <td>Tanggal Lahir : </td>
     <td></td>
     <td> <input type="date" name="date" /></td>
    </tr>
    <tr>
        <td>Nama Orang Tua :  </td>
        <td></td>
        <td><input type="text" name="parent" size="22" placeholder="Masukan Nama Orang Tua"></td>
    </tr>
    <tr>
        <td>No.HP Orang Tua : </td>
        <td></td>
        <td><input type="text" name="telp" size="22" placeholder="Masukan No Telepon"></td>
    </tr>
    <tr>
        <td>Provinsi</td>
        <td></td>
        <td><select name="prov">
<option value="-Pilih-">Pilih </option>
<option value="Aceh">Aceh</option>
<option value="Sumatera Utara">Sumatera Utara</option>
<option value="Sumatera Barat">Sumatera Barat</option>
<option value="Riau">Riau</option>
<option value="Jambi">Jambi</option>
<option value="Sumatera Selatan">Sumatera Selatan</option>
<option value="Bengkulu">Bengkulu</option>
<option value="Lampung">Lampung</option>
<option value="DKI Jakarta">DKI Jakarta</option>
<option value="Jawa Barat">Jawa Barat</option>
<option value="Jawa Tengah">Jawa Tengah</option>
<option value="DI Yogyakarta">DI Yogyakarta</option>
<option value="Jawa Timur">Jawa Timur</option>
<option value="Banten">Banten</option>
<option value="Nusa tenggara Timur">Nusa Tenggara Timur</option>
<option value="Nusa tenggara Barat">Nusa Tenggara Barat</option>
<option value="Kalimantan Utara">Kalimantan Utara</option>
<option value="Kalimantan Barat">Kalimantan Barat</option>
<option value="Kalimantan Tengah">Kalimantan Tengah</option>
<option value="Kalimantan Selatan">Kalimantan Selatan</option>
<option value="Kalimantan Timur">Kalimantan Timur</option>
<option value="Sulawesi Utara">Sulawesi Utara</option>
<option value="Sulawesi Selatan">Sulawesi Selatan</option>
<option value="Sulawesi Tenggara">Sulawesi Tenggara</option>
<option value="Sulawesi Tengah">Sulawesi Tengah</option>
<option value="Maluku">Maluku</option>
<option value="Maluku Utara">Maluku Utara</option>
<option value="Papua">Papua</option>
<option value="Papua Barat">Papua Barat</option>
</select></td>
    </tr>
<tr>
    <td>Kota :  </td>
    <td></td>
    <td>
        <select name="Kota">
            <php
            if ($value= "Aceh") {
            ?>
        <option value="Banda Aceh"> Banda Aceh </option>
        <option value="Merauke">Merauke</option>
        <php
             }
        ?>
        
        </select>
    </td>
</tr>