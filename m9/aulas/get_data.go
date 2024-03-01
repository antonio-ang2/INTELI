package main

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/lib/pq"
)

// Parâmetros de conexão com o banco de dados
const (
	hostname = "database-stations.cxic0so62a43.us-east-1.rds.amazonaws.com"
	username = "postgres"  // Substitua pelo seu nome de usuário
	password = "admin1234" // Substitua pela sua senha
	database = "postgres"  // Substitua pelo nome do seu banco de dados
)

// Função para executar consultas SQL SELECT
func selectData(table string) {
	connStr := fmt.Sprintf("host=%s user=%s password=%s dbname=%s sslmode=disable", hostname, username, password, database)
	db, err := sql.Open("postgres", connStr)
	if err != nil {
		log.Fatal("Erro ao conectar ao banco de dados:", err)
	}
	defer db.Close()

	rows, err := db.Query(fmt.Sprintf("SELECT * FROM %s", table))
	if err != nil {
		log.Fatal("Erro ao executar consulta:", err)
	}
	defer rows.Close()

	fmt.Printf("Dados da tabela %s:\n", table)
	for rows.Next() {
		var id int
		var column1 string
		var column2 string
		// Defina os tipos de suas colunas conforme necessário

		err := rows.Scan(&id, &column1, &column2) // Adicione mais variáveis de acordo com o número de colunas e seus tipos
		if err != nil {
			log.Fatal("Erro ao ler linha:", err)
		}
		fmt.Println(id, column1, column2) // Substitua por seu processamento de dados
	}
	err = rows.Err()
	if err != nil {
		log.Fatal(err)
	}
}
