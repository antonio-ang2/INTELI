package main

import (
	"database/sql"
	"fmt"
	"log"

	"github.com/lib/pq"
)

// Dados fictícios para inserção nas tabelas
var estacoesData = [][]interface{}{
	{1, 36.000000, 16.000000},
}

var gasData = [][]interface{}{
	{1, 1, 526.000000, 7.000000, 343.000000, 404.000000, 179.000000},
}

var radLumData = [][]interface{}{
	{1, 1, 267.000000, 3.000000, 241.000000},
}

// Função para inserir dados nas tabelas
func insertData(tableName string, data [][]interface{}) {
	connStr := fmt.Sprintf("host=%s user=%s password=%s dbname=%s sslmode=disable", hostname, username, password, database)
	db, err := sql.Open("postgres", connStr)
	if err != nil {
		log.Fatal("Erro ao conectar ao banco de dados:", err)
	}
	defer db.Close()

	txn, err := db.Begin()
	if err != nil {
		log.Fatal("Erro ao iniciar transação:", err)
	}

	stmt, err := txn.Prepare(pq.CopyIn(tableName, "col1", "col2", "col3", "col4", "col5", "col6", "col7"))
	if err != nil {
		log.Fatal("Erro ao preparar declaração:", err)
	}

	for _, entry := range data {
		_, err := stmt.Exec(entry...)
		if err != nil {
			log.Fatal("Erro ao inserir linha:", err)
		}
	}

	_, err = stmt.Exec()
	if err != nil {
		log.Fatal("Erro ao finalizar declaração:", err)
	}

	err = stmt.Close()
	if err != nil {
		log.Fatal("Erro ao fechar declaração:", err)
	}

	err = txn.Commit()
	if err != nil {
		log.Fatal("Erro ao cometer transação:", err)
	}

	fmt.Printf("Dados inseridos na tabela %s com sucesso!\n", tableName)
}

func main() {
	insertData("Estacao", estacoesData)
	insertData("Gas", gasData)
	insertData("Rad_lum", radLumData)
}
