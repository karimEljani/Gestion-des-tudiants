# EmployeeWebAPI – ASP.NET Core Web API (.NET 8)

Solution :
- `MesClasses`      : bibliothèque de classes (Employee, Department, Gender)
- `EmployeeWebAPI`  : Web API (EF Core + SQL Server LocalDB, Repository Pattern, Swagger)

## Lancer le projet
1. Ouvrir `EmployeeWebAPI.sln` dans Visual Studio 2022 (SDK .NET 8).
2. Package Manager Console (projet par défaut = EmployeeWebAPI) :
   ```
   Add-Migration InitialCreate
   Update-Database
   ```
   (ou en CLI, depuis le dossier EmployeeWebAPI :
   `dotnet ef migrations add InitialCreate` puis `dotnet ef database update`)
3. F5 -> Swagger : https://localhost:7262/swagger

## Endpoints
| URI                                         | Verbe  | Résultat                  |
|---------------------------------------------|--------|---------------------------|
| /api/employees                              | GET    | Liste des employés        |
| /api/employees/1                            | GET    | Employé Id = 1            |
| /api/employees                              | POST   | Crée un employé (201)     |
| /api/employees/1                            | PUT    | Modifie l'employé Id = 1  |
| /api/employees/1                            | DELETE | Supprime l'employé Id = 1 |
| /api/employees/search?name=zribi&gender=0   | GET    | Recherche                 |
| /api/departments, /api/departments/1        | GET    | Départements              |

Exemple de corps JSON (POST) :
```json
{
  "firstName": "BEN ALI",
  "lastName": "SOFIEN",
  "email": "sofien@example.com",
  "dateOfBrith": "1976-05-10",
  "gender": 1,
  "departmentId": 1,
  "photoPath": null
}
```
